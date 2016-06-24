sudo apt update
sudo apt upgrade
sudo apt dist-upgrade

# Utils
sudo apt install vim
sudo apt install curl
sudo apt install httpie

sudo apt install libjpeg-dev libpng-dev libfreetype-dev libhdf5-dev

# Gnome Shell Extensions
sudo add-apt-repository ppa:ne0sight/chrome-gnome-shell
sudo apt update
sudo apt install libindicator7 libappindicator1
sudo apt-get f install
sudo apt install chrome-gnome-shell

# dash-to-dock drop-down-terminal shellshape todo workspace-grid put-windows applications-menu refresh-wifi-connections

# Git
sudo add-apt-repository ppa:git-core/ppa
sudo apt-get update
sudo apt install git
git config --global user.name "Romain Lepert"
git config --global user.email "romlepert@gmail.com"

# Python
sudo pip install --upgrade pip
sudo apt install python-virtualenv
sudo apt install python-dev python3-dev
sudo apt install python-flake8 python-flake8-docstrings python-hacking
sudo pip install virtualenvwrapper  # edit .bashrc to complete installation
sudo pip install jupyter

# Node.js v6.x
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install -y nodejs

sudo npm install -g bower
sudo npm install -g gulp
sudo npm install -g lodash graceful-fs  # update deprecated modules

# MySQL
sudo apt install mysql-server mysql-client libmysqlclient-dev
# sudo apt-get install mysql-common

# Atom (not official PPA repository)
sudo add-apt-repository ppa:webupd8team/atom
sudo apt-get update
sudo apt-get install atom
# apm list --installed --bare > packages.txt
# apm install --packages-file packages.txt
# apm stars --install --user obust
