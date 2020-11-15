#!/bin/sh

# ref: https://docs.influxdata.com/telegraf/v1.12/introduction/installation/
#########################################################################################################################
# INFLUXDB could be installed with install_influxdb.sh script, 
# BUT ---- ALTERNATIVELY
# INFLUXDB could also be installed as follows.




# Before adding Influx repository, run this so that apt will be able to read the repository.

sudo apt-get update -y 
sudo apt-get install apt-transport-https

# Add the InfluxData key

wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -
source /etc/os-release
test $VERSION_ID = "7" && echo "deb https://repos.influxdata.com/debian wheezy stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
test $VERSION_ID = "8" && echo "deb https://repos.influxdata.com/debian jessie stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
test $VERSION_ID = "9" && echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
test $VERSION_ID = "10" && echo "deb https://repos.influxdata.com/debian buster stable" | sudo tee /etc/apt/sources.list.d/influxdb.list

# install and start
sudo apt-get update -y 
sudo apt-get install influxdb -y
sudo service influxdb start

#sudo systemctl start influxdb
#sudo systemctl enable influxdb
