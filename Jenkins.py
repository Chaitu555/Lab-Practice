Jenkins Level 1 Tasks
#The DevOps team at xFusionCorp Industries is initiating the setup of CI/CD pipelines and has decided to utilize Jenkins as their server. Execute the task according to the provided requirements: 
#1. Install Jenkins on the jenkins server using the apt utility only, and start it using the service command. If you face a timeout issue while starting the Jenkins service, first check the service status with service jenkins status Then review the logs in /var/log/jenkins/jenkins.log to identify the cause.
#2. Jenkin's admin user name should be theadmin, password should be Adm!n321, full name should be Kirsty and email should be kirsty@jenkins.stratos.xfusioncorp.com.
#Note: 1. To access the jenkins server, connect from the jump host using the root user with the password S3curePass. 
#2. After Jenkins server installation, click the Jenkins button on the top bar to access the Jenkins UI and follow on-screen instructions to create an admin user.

# The Steps i followed to complete this task
ssh to thor@jump-host
Then ssh root@jenkins (Pass S3curePass) from thor@jump-host   ----- (We have used root as it was mentioned in the question)
apt update
apt install openjdk-17-jdk -y   -- Version changes on the usage
java -version    --- Checking the version

wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io.key   --- For adding the Jenkins Key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" > /etc/apt/sources.list.d/jenkins.list     ---- Add Repo with Signed Key
service jenkins start   --- For checking weather the Jenkins is starting or not
#If jenkins is failing to start follow this step
cat /var/log/jenkins/jenkins.log    ---- This exactly shows the issue why jenkins is not started (Mainly version mismatch)
service jenkins restart   --- Restart the jenkins
#If there are multiple Java versions are downloaded this helps to select the required version
update-alternatives --config java   -- Select the requires one based on the latest version (Max option 2 will be the fresh)
#For Ensuring the Jenkins is using the exact Java version
vi /etc/default/jenkins
JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64   --- Need to add this line if u have not found JAVA_HOME
service jenkins restart
service jenkins status   --- This helps to find weather the jenkins is running or not


