#!/bin/bash
cd srv/jimminycricket2
sudo cp /srv/jimminycricket2/config/jimminycricket.service /etc/systemd/system/
sudo cp /srv/jimminycricket2/config/jimminycricket.conf /etc/apache2/sites-available/
sudo a2dissite *.conf
sudo a2ensite jimminycricket.conf
sudo apt update && sudo apt install python3.12-venv python3-pip apache2 -y
sudo apt-get install python3-dev libmysqlclient-dev -y
pip3 install virtualenv
python3 -m venv /srv/jimminycricket2/venv
source /srv/jimminycricket2/venv/bin/activate
pip3 install -r /srv/jimminycricket2/requirements.txt