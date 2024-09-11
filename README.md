# open_bioreactor

## Installing Ansible on a Raspberry Pi
Assumptions:
1.) Running on Raspberry Pi 4+
```
sudo cat /sys/firmware/devicetree/base/model;echo
sudo apt update
sudo apt install -y software-properties-common
sudo apt install -y ansible
ansible --version 
```

Setup Log
```
id
clear
cd /etc/
sudo mkdir ansible
sudo vi /etc/ansible/ansible.cfg
sudo vi /etc/ansible/hosts
cat /etc/ansible/hosts 
ping 192.168.1.147
ansible myservers -m ping -u pi --ask-pass
which sshpass
```

TODOs
* Write a python 3 script to automate the setup PXE Boot server for Raspberry Pi
* If there is automation gap PXE left, then write a python 3 script to automate ansible setup for Raspberry Pi

## Reference
* [full example](https://qmacro.org/blog/posts/2020/04/05/initial-pi-configuration-via-ansible/)
* [git repo](https://github.com/mkuthan/raspberry-ansible)
* [simple example](https://medium.com/@tisutisu/installing-ansible-on-a-raspberry-pi-cc3ea79edc05)
* [PXE Boot](https://www.howtoraspberry.com/2022/03/how-to-pxe-boot-a-raspberry/)
