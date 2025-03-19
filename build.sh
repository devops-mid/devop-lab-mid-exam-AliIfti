#!/bin/bash

echo "Building the application..."

# Step 1: Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Step 2: Apply database migrations (if using Flask-Migrate)
echo "Applying database migrations..."
flask db upgrade

# Step 3: Build or prepare static assets (if needed)
echo "Preparing static files..."
# Example: Copy static files or collect assets (modify if necessary)
mkdir -p static
cp -r templates static/

echo "Build process completed successfully!"

