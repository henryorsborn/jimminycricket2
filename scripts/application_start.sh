#!/bin/bash
cd srv/jimminycricket2
sudo systemctl daemon-reload
sudo service jimminycricket start
sudo service jimminycricket restart
