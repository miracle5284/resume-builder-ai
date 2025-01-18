#!/bin/bash

# Load the config file
CONFIG_FILE="config.env"

if [ -f "$CONFIG_FILE" ]; then
  source "$CONFIG_FILE"

  ENV_FILE_PATH=$(echo "$ENV_FILE_PATH" | sed 's/[[:space:]]*$//')
  DOCKER_COMPOSE_FILE=$(echo "$DOCKER_COMPOSE_FILE" | sed 's/[[:space:]]*$//')
  SECRETS_COMPOSE_FILE=$(echo "$SECRETS_COMPOSE_FILE" | sed 's/[[:space:]]*$//')

else
  echo "Configuration file ($CONFIG_FILE) not found. Please create it and set ENV_FILE_PATH, DOCKER_COMPOSE_FILE, and SECRETS_COMPOSE_FILE."
  exit 1
fi

if [ -z "$ENV_FILE_PATH" ]; then
  echo "ENV_FILE_PATH is not set in the configuration file. Please set it to the path of your .env file."
  exit 1
fi

if [ ! -f "$ENV_FILE_PATH" ]; then
  echo "The .env file at $ENV_FILE_PATH does not exist. Please provide a valid path."
  exit 1
fi

if [ -z "$DOCKER_COMPOSE_FILE" ]; then
  echo "DOCKER_COMPOSE_FILE is not set in the configuration file. Please set it to the path of your docker-compose.yml."
  exit 1
fi

if [ ! -f "$DOCKER_COMPOSE_FILE" ]; then
  echo "The DOCKER_COMPOSE_FILE at $DOCKER_COMPOSE_FILE does not exist. Please provide a valid path."
  exit 1
fi

if [ -z "$SECRETS_COMPOSE_FILE" ]; then
  echo "SECRETS_COMPOSE_FILE is not set in the configuration file. Please set it to the path of your docker-compose.secrets.yml."
  exit 1
fi

# Ensure Docker Swarm is active
if ! docker info 2>/dev/null | grep -q 'Swarm: active'; then
  echo "Docker Swarm is not initialized. Initializing now..."
  docker swarm init
fi

# Initialize secrets and the list of secrets for services
secrets_section="secrets:"
services_secrets_list=""

# Read secrets from the .env file and process them
while IFS= read -r line || [ -n "$line" ]; do
  if [[ "$line" =~ ^[A-Za-z][A-Za-z0-9_-]*[[:space:]]*=[[:space:]]*.* ]]; then
    key=$(echo "$line" | cut -d '=' -f 1 | xargs)
    value=$(echo "$line" | cut -d '=' -f 2- | xargs)

    if [[ ! "$key" =~ ^[a-zA-Z0-9]([a-zA-Z0-9_.\-]{0,62}[a-zA-Z0-9])?$ ]]; then
      echo "Error: Invalid secret name '$key'. Skipping..."
      continue
    fi

    # Validate the key (Docker secret name)
    if docker secret ls | grep -q -w "$key"; then
      docker secret rm "$key" >/dev/null 2>&1
      if [[ $? -ne 0 ]]; then
        echo "Error: Failed to remove existing secret '$key'. Skipping..."
        continue
      fi
    fi

    echo "$value" | docker secret create "$key" - >/dev/null 2>&1
    if [[ $? -eq 0 ]]; then
      echo "Secret $key created/updated successfully."
    else
      echo "Error: Failed to create/update secret '$key'."
    fi

    # Add the secret to the secrets section
    secrets_section+="
  $key:
    external: true"

    # Add the secret to the services secrets list
    services_secrets_list+="\"$key\","
  fi
done < "$ENV_FILE_PATH"

# Remove trailing comma from services_secrets_list
services_secrets_list="[${services_secrets_list%,}]"

# Modify the services section to include the secrets list
echo "Modifying services section to include secrets..."
yq e ".services.web.secrets = $services_secrets_list" "$DOCKER_COMPOSE_FILE" > "$SECRETS_COMPOSE_FILE"

# Append the secrets section to the new compose file
echo "$secrets_section" >> "$SECRETS_COMPOSE_FILE"

echo "Secrets compose file ($SECRETS_COMPOSE_FILE) created successfully."
