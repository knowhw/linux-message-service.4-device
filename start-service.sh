#!/bin/sh
sudo systemctl stop devices.service 
# devix

sudo systemctl daemon-reload
sudo systemctl enable --now devices.service  
sudo systemctl restart devices.service 

sudo systemctl status devices.service 
