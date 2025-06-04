@echo off
REM Installation script for Gravlosa Chatbot (Windows)

ECHO Setting up your Gravlosa environment...

python -m venv venv
call venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt

ECHO Setup complete. Run it with:
ECHO streamlit run app.py
