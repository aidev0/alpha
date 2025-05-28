#!/bin/bash

# Exit on error
set -e

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Upgrade pip
echo "Upgrading pip..."
venv/bin/pip install --upgrade pip

# Install requirements
echo "Installing requirements..."
venv/bin/pip install -r requirements.txt

echo "Virtual environment is ready!"
echo ""
echo "To activate the virtual environment, run:"
echo "source venv/bin/activate"
echo ""
echo "You should see (venv) at the start of your prompt when activated." 