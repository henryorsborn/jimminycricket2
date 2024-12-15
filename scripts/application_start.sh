#!/bin/bash
cd /srv/jimminycricket2
sudo systemctl daemon-reload
sudo service jimminycricket stop
sudo service jimminycricket start
