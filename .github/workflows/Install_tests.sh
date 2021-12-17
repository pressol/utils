#!/bin/bash
# install megacmd
# get install package
megacmd="https://mega.nz/linux/MEGAsync/xUbuntu_20.04/amd64/megacmd_1.4.0-5.1_amd64.deb"
wget $megacmd
# install 
sudo apt install -y megacmd_1.4.0-5.1_amd64.deb
