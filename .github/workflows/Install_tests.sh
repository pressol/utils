#!/bin/bash
# install other software
sudo add-apt-repository universe
sudo apt update
sudo apt install -y p7zip-full p7zip-rar
# install megacmd if required
if command -v dpkg -l | grep megacmd &> /dev/null
then
    # get install package
    megacmd="https://mega.nz/linux/MEGAsync/xUbuntu_20.04/amd64/megacmd_1.4.0-5.1_amd64.deb"
    wget $megacmd
    ls -l
    # install 
    sudo apt install -y ./megacmd_1.4.0-5.1_amd64.deb
fi