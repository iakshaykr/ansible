#!/usr/bin/python
import os

os.system(' sudo apt update')

os.system('sudo apt install software-properties-common')

os.system('sudo apt-add-repository --yes --update ppa:ansible/ansible')

os.system('sudo apt install ansible')

exit

