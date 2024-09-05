#!/bin/bash
# Install Python and pip if they are not available
if ! command -v python3 &> /dev/null; then
    apt-get update && apt-get install -y python3 python3-pip
fi


pip3 install -r requirements.txt
python3.9 manage.py migrate
python3.9 manage.py collectstatic
