from fastapi import FastAPI
app=FastAPI()
@app.get('/')
def r(): return {'Hello':'Docker'}

"Hello: World"
age = 25,
print

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

sudo chmod 755 /tmp/xfusioncorp.sh
# For giving the permission to the all users in organisation. In this i have saved this in /tmp location but in real time we won't save them there due to security issues.Because any one can edit or delete the file

#For connecting to other/multiple servers we need to generate the SSH key on the main server and then need to copy and save them on the other servers
ls ~/.ssh    ----- # to check weather the keys are existed or not
ssh keygen -t rsa -b 2048
# -t & RSA means the type of key we need to generate && -b 2048 indicates the RSA key length -- the longer the bit, the higher the security will be added t key. 
Example
Type	    Security	    Recommended Today?
RSA2048	  Good       	  Acceptable
RSA4096	  Stronger   	  Slower
ED25519	  Very Strong	  Bestchoice

#For setting up no permissions for a user with ACL Commands 
#Mainly ACL cmds are used to override the traditional permissions for a particular user. ACL gives more flexibility for permissions
sudo setfacl -m u:chaitu:--- /etc/hostname
#setfacl --- Set File Access Control List 
#-m  --- Modify (ACL file)
#u:chaitu:---     --- user name with read write execute permission  (ex : r--,-r-) 
#etc/hostname  --- Target file
getfacl /etc/hostname #For checking the file permissions after setup

#For replacing a particular word ia a file -- we use sed command
sed -i 's/Oldname/Newname/g' /root/filename
#-i -- modify Directly
#s -- Substitue 
#g -- Global 

#For copying file securly form one server to other -- login to 1st server with the credentials and use the cmd
scp /tmp/nautilus.txt.gpg banner@stapp03.stratos.xfusioncorp.com:/home/web/     
# After scp the path of the file need to be transfered following with the 2nd server ID and :/hom/web/  the path where we are copying

#Crontab access control for the users with cron.allo && cron.deny cmds
sudo vi /etc/cron.allow 
type the name which we need to allow for the cron jobs to create/edit

sudo vi /etc/cron.deny
#for restriciting the user to create/ edit the cron jobs

#for setting the time zone
sudo timedatectl set-timezone America/Jamaica                                   

#For setting the limitations for a user with maximum and minimum creation.
sudo vi /etc/security/limits.conf
#In the file itself we need to mention the user name and thier limitations (for example :  soft limit to 1027 && hard limit to 2026)

#For installing tomcat and changing the access port to 6200 including copying the ROOT.war file from jumphost to appserver
1. On main server check the ROOT.war file Login to the required appserver (ssh to server)
2. install tomcat (sudo yum install -y tomcat) --- from here done On 2nd server
3. sudo systemctl enable tomcat 
4. sudo vi /etc/tomcat/server.xml  ---- Here we need to edit the port number
5. Exit from appserver and scp the ROOT.war file (/tmp/ROOT.war) to the appserver from main server   ---- (scp /tmp/ROOT.war name@appserver:/tmp)                                                                                                   
6. Login to appserver now and use the sudo mv /tmp/ROOT.war /var/lib/tomcat/webapps/    for pasting the ROOT.war file
7. sudo systemctl start tomcat
8. sudo systemctl status tomcat
9. curl http://appserver:6200

GIT
#cloning file from one repo to other repo
Log into the required server
ls path    # so that we can get the confirmation any files are located or not
git clone path of 1st repo followed by 2nd repo path   (Ex: git clone /opt/games.git  /usr/src/kodekloudrepos/games)
ls # need to check weather the files are been copied or not
cd /usr/src/kodekloudrepos/games  
ls -a  # Confirming the .git file exits or not
git remote -v #Verifying the origin

#Forkingt the Repo
Need to login with the credetials and search for the repo that is required to fork
On the top right corner you can find the fork option

#Copy the sample file and within the cloned repo & add, commit and then push to the Main branch
ssh thor@jump_host.stratos.xfusioncorp.com
scp /tmp/index.html natasha@ststor01.stratos.xfusioncorp.com:/tmp
ssh natasha@ststor01.stratos.xfusioncorp.com
cd /usr/src/kodekloudrepos/blog
cp /tmp/index.html .
git add index.html
git commit -m "Added sample index.html file"
git push origin master

git commit --global --add safe.directory 
