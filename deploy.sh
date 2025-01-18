#!/bin/bash

set -e

CONFIG_FILE="config.env"

if [ -f "$CONFIG_FILE" ]; then
  source "$CONFIG_FILE"

  DOCKER_COMPOSE_FILE=$(echo "$DOCKER_COMPOSE_FILE" | xargs)
  SECRETS_COMPOSE_FILE=$(echo "$SECRETS_COMPOSE_FILE" | xargs)
else
  echo "Configuration file ($CONFIG_FILE) not found. Please create it and set ENV_FILE_PATH, DOCKER_COMPOSE_FILE, and SECRETS_COMPOSE_FILE."
  exit 1
fi

./install.sh

echo "Loading secrets..."
./load-docker-env.sh

echo "Building the Docker image..."
#docker builder prune
docker build --no-cache -t multi_agent_chatbot_image:latest .

echo "Deploying the ai_agent_stack..."
docker stack deploy -c "$SECRETS_COMPOSE_FILE" ai_agent_stack

echo "Checking stack status"
docker stack ps ai_agent_stack

echo "Done"