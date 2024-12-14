#!/bin/bash
sudo apt update
sudo apt clean
sudo apt install python3.12-venv python3-pip apache2
cd /srv/jimminycricket2/
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
sudo adduser --system --no-create-home --group gunicorn
sudo chown -R gunicorn:gunicorn /srv/jimminycricket2/
sudo cp /srv/jimminycricket2/config/jimminycricket.conf /etc/apache2/sites-available/
sudo a2enmod proxy proxy_http
sudo service apache2 reload
sudo snap install --classic certbot
sudo a2dissite *.conf
sudo a2ensite jimminycricket.conf
sudo cp /srv/jimminycricket2/config/jimminycricket.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable jimminycricket
sudo service jimminycricket start
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo certbot --apache -d hwors-jimminycricket-stg.com -d www.hwors-jimminycricket-stg.com
sudo crontable -e 0 4 * * 1 /usr/bin/certbot --renew && /usr/sbin/service apache2 reload
