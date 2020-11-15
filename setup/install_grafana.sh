#!/bin/sh

# ref: https://grafana.com/grafana/download?platform=arm
sudo apt-get install -y adduser libfontconfig1
wget https://dl.grafana.com/oss/release/grafana_7.0.4_armhf.deb
sudo dpkg -i grafana_7.0.4_armhf.deb

# ref: https://grafana.com/docs/grafana/latest/installation/debian/
sudo systemctl daemon-reload
sudo systemctl start grafana-server
#sudo systemctl status grafana-server

# ref: https://www.youtube.com/watch?v=pE7zU4MOqC8
# startup 
#sudo systemctl enable grafana-server.service
#sudo systemctl enable grafana-server 
