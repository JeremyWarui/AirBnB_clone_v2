#!/usr/bin/env bash
#configuration file
#nginx string to replace with
NEWSTR="\\\t\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"

#install nginx
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start

#make directories
#/data/web_static/releases/test
#/data/web_static/shared
sudo mkdir -p /data/web_static/{releases/test,shared}

# create a sample html
sudo echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"| sudo tee /data/web_static/releases/test/index.html

#create symbolic link of test to current folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#give ownership to user and group to ubuntu
sudo chown -Rh ubuntu:ubuntu /data/

#configure the nginx 
sudo sed -i "47i $NEWSTR" /etc/nginx/sites-available/default

#restart
sudo service nginx restart
