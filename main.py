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

# Installing the package on a multiple servers and adding the cronjob for them
sudo yum install -y cronie
#Here we are installing cronie on a particular server without interaction of second command by using -y after install
sudo systemctl start crond && sudo systemctl enable crond
#For envoking the crond and for checking weather it is enabled on it
sudo systemctl status crond
#This helps in checking the crond is running or not ex: active(running)
sudo crontab -e
#For opening the shell where we need to write the cronjob
*/5 * * * * echo hello > /tmp/cron_text   -- #It helps to run the job for every 5 minutes and saves to /tmp/cron_text file
#Every 5 minutes -- Every hour -- Every day -- Every month -- Every weekday


