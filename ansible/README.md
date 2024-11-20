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

# Run ping
```
ansible all -m ping        
[WARNING]: Platform linux on host raspberry_1 is using the discovered Python interpreter at /usr/bin/python3.9, but future installation
of another Python interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-
core/2.17/reference_appendices/interpreter_discovery.html for more information.
raspberry_1 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3.9"
    },
    "changed": false,
    "ping": "pong"
}
```

# Run the playbook
```
ansible-playbook setup.yaml
```
