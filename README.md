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
## Reference
* [full example](https://qmacro.org/blog/posts/2020/04/05/initial-pi-configuration-via-ansible/)
* [git repo](https://github.com/mkuthan/raspberry-ansible)
* [simple example](https://medium.com/@tisutisu/installing-ansible-on-a-raspberry-pi-cc3ea79edc05)
