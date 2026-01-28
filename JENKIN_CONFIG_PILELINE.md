STEP 1️⃣ Create Pipeline Job

Jenkins Dashboard

Click New Item

Name:

github-actions-jenkins-pipeline


Select Pipeline

Click OK

✅ What to select NOW

👉 Select: Pipeline (first option)

❌ Don’t choose Freestyle
❌ Don’t choose Multibranch (we’ll do that later)

Pipeline = real DevOps / real company standard ✅

📝 Job Name (important)

At the top field, enter:

github-actions-jenkins-pipeline


(No spaces is best practice)

Then click OK.

2️⃣ In Pipeline section set EXACTLY this

Definition

Pipeline script from SCM


SCM

Git


Repository URL

https://github.com/ranjan-fullstack/devops-assessn


Credentials

None   (OK because public repo)


Branches to build

*/main


Script Path

Jenkinsfile


🧱 STEP 1A: Install Docker on Jenkins EC2 (if not already)

docker --version

sudo yum install docker -y
sudo systemctl start docker
sudo systemctl enable docker


🔑 STEP 1B: Give Jenkins permission to run Docker (VERY IMPORTANT)

By default, Jenkins cannot run docker.

Run:

sudo usermod -aG docker jenkins
sudo usermod -aG docker ec2-user


Restart services:

sudo systemctl restart docker
sudo systemctl restart jenkins


✅ Verify (quick check)
sudo -u jenkins docker ps