#!/bin/sh

# ref: https://docs.influxdata.com/influxdb/v1.7/introduction/installation/

sudo apt-get update -y 
sudo apt-get install apt-transport-https

# add source
wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -
source /etc/os-release
echo "deb https://repos.influxdata.com/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/influxdb.list

# install and start
sudo apt-get update -y
sudo apt-get install influxdb -y
sudo service influxdb start
#sudo systemctl start influxdb
