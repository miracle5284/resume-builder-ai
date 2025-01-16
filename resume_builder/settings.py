from pathlib import Path

# Base directory for the project
BASE_DIR = Path(__file__).resolve().parent

# Directories for temporary and exported files
TEMP_DIR = BASE_DIR / 'assets/tmp'
DOWNLOADS_DIR = BASE_DIR / 'assets/export'