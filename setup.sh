#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt

# Add the cron job
(crontab -l 2>/dev/null; echo "*/10 * * * * /path/to/your/script/main.py") | crontab -

# Make sure the Python script is executable
chmod +x ./src/main.py
