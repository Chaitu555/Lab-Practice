from fastapi import FastAPI
app=FastAPI()
@app.get('/')
def r(): return {'Hello':'Docker'}

from fastapi import FastAPI
app=FastAPI()
@app.get('/')
def r(): return {'Hello':'Git'}

from fastapi i port FastAPI
app=FastAPI()
@app.get('/')
def r(): return {'Hello':'K8s'}

"Hello: World"
age = 25,
print(age) 

pwd, cd, cd., cd .., ls, ls -lt, ls -lrt, mkdir
ssh john@jump_host_company.com
password yes
sudo groupadd Family
sudo useradd chaitu
sudo usermod -aG Family chaitu

# Restarting the sshd helps to implement the changes done in the script
sudo systemctl restart sshd

# For installing the SELinux on the server with the multiple packages
sudo yum install -y selinux-policy selinux-policy-targeted policycoreutils
#sudo  --------------------- for running the cmd with root access
# yum  --------------------- package manager used for RHEL,CentOS,Rocky Linux, AlmaLinux
#-y    --------------------- For executig the yes permission without any extra permission
#selinux-policy ------------ It contains core security rules and defenetions
#selinux-policy-targeted  --- commonly used policy which contains multiple policies 
#a) targeted (default)
#b) strict (very restrictive)
#c) mls (military-level security)
#Policycoreutils ------------Tools to manage SELinux.
#For example:getenforce; setenforce; restorecon; semanage


