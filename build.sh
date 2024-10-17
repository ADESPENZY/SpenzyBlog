#!/bin/bash
echo "Starting the build process..."

set -o errexit  # Exit immediately if a command exits with a non-zero status

# Install required packages
pip install -r requirements.txt  # Install dependencies listed in requirements.txt

# Collect static files
python manage.py collectstatic --noinput  # Collect static files for deployment
python manage.py migrate  # Apply database migrations

echo "Build complete!"  # Notify that the build process is complete