#!/bin/bash
# Installation script for Gravlosa Chatbot

echo "Setting up your Gravlosa environment..."

# Create virtual environment if not exists
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
openai migrate
pip install openai==0.28



echo "Gravlosa setup complete. Run it with:"
echo "streamlit run app.py"
