import os
from pathlib import Path


# Base directory for the project
BASE_DIR = Path(__file__).resolve().parent

# Directories for temporary and exported files
TEMP_DIR = BASE_DIR / 'assets/tmp'
DOWNLOADS_DIR = BASE_DIR / 'assets/export'

def load_secrets(secrets_dir='/run/secrets'):
    """Load secrets from the docker secrets"""
    if os.path.exists(secrets_dir):
        for secret_name in os.listdir(secrets_dir):
            secret_path = os.path.join(secrets_dir, secret_name)
            with open(secret_path, 'r') as fp:
                os.environ[secret_name] = fp.read().strip()

load_secrets()