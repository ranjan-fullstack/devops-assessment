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

Implemented Jenkins pipeline to build multiple microservice Docker images (frontend & backend) from a single GitHub repository using service-specific Dockerfiles.


🔐 STEP 2A: Create Docker Hub Credentials in Jenkins

Open Jenkins → Manage Jenkins → Credentials

Click (global) → Add Credentials

Fill like this:

Kind: Username with password

Username: <your-dockerhub-username>

Password: <your-dockerhub-password or access token>

ID: dockerhub-creds ✅ (important)

Description: Docker Hub credentials

Click Save

👉 Pro tip: If you have 2FA on Docker Hub, use an Access Token (best practice).



• Designed and implemented a Jenkins declarative pipeline to build and push multiple Docker images (frontend and backend) to Docker Hub using secure credential management.
• Integrated GitHub SCM with Jenkins on AWS EC2 to automate containerized CI workflows.
• Followed industry best practices including multi-service builds, credential isolation, and post-build cleanup.

I containerized backend and frontend separately, deployed them using Docker Compose on EC2, and automated redeployment via Jenkins after every GitHub push.