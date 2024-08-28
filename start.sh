#!/bin/sh
#sudo systemctl stop test.socket 

#sudo systemctl daemon-reload
#sudo systemctl enable --now test.socket 
# sudo systemctl restart dc-launcher.service

#sudo systemctl status test.socket

#
#sudo apt autoremove deepin-picker -y
#sudo apt install deepin-picker -y


# sudo systemctl stop usb-devices.service 

# sudo systemctl daemon-reload
# sudo systemctl enable --now usb-devices.service 
# sudo systemctl restart dc-launcher.service

# sudo systemctl status usb-devices.service


sudo systemctl stop devices.service 
# devix

sudo systemctl daemon-reload
sudo systemctl enable --now devices.service  
sudo systemctl restart devices.service 

sudo systemctl status devices.service 
