#! /bin/bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install --upgrade pip
python app.py