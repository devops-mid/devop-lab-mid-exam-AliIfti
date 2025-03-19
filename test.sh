#!/bin/bash

echo "Running tests..."

# Step 1: Ensure dependencies are installed
echo "Installing dependencies..."
pip install -r requirements.txt

# Step 2: Run unit tests using pytest
echo "Executing unit tests..."
pytest tests/ --disable-warnings --cov=app


echo "Tests completed!"

