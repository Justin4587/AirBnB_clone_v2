#!/usr/bin/env bash
# happy little comment

sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
sudo echo "My Existance is Miserable" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo service nginx stop
location="/etc/nginx/sites-enabled/default"
sudo sed -i '43i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' $location
sudo service nginx restart
