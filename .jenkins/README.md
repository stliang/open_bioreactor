Jenkins might not be aware of the PATH where Ansible is installed. Update the PATH in Jenkins:

Go to Manage Jenkins → Manage Nodes
Under Node Properties, check Environment variables.
Add or update the PATH variable to include the directory where ansible-playbook is installed. For example:
```
/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
```