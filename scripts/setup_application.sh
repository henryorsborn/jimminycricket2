#!/bin/bash
cd srv/jimminycricket2
sudo apt update && sudo apt install python3.12-venv python3-pip apache2
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
