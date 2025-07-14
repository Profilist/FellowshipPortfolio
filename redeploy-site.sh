#!/bin/bash

SERVICE_NAME="myportfolio.service"
DIR_PATH="/root/FellowshipPortfolio"
VENV="$PATH/python3-virtualenv"
FLASK_APP="app.py"

cd "$DIR_PATH"
git fetch && git reset origin/main --hard
source "$VENV/bin/activate"
pip install -r "requirements.txt"

sudo systemctl daemon-reload
sudo systemctl restart "$SERVICE_NAME"
sudo systemctl status "$SERVICE_NAME"
