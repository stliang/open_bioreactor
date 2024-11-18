# Install ansible

# Set hosts file
sudo vi /etc/ansible/hosts
```
[all:vars]
ansible_connection=ssh
ansible_ssh_user=*******
ansible_ssh_pass=******

[raspberry]
raspberry_1 ansible_host=192.168.1.147
```
