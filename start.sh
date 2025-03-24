#!/bin/bash
source venv/Scripts/activate
pip install -r requirements.txt
cd cukrark
./manage.py runserver
