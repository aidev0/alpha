#!/bin/bash

# Setup virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate
echo "✅ Virtual environment activated"

# Install dependencies
echo "Installing dependencies..."
pip install fastapi motor pymongo "uvicorn[standard]" python-dotenv pydantic

# Copy environment variables if needed
[ ! -f ".env" ] && grep "MONGODB" ../.env > .env 2>/dev/null

# Start the API server
echo "🎉 Starting Alpha at http://localhost:8001/docs"
echo "🛑 Press Ctrl+C to stop"
python api.py