DevOps Setup, Deployment & Troubleshooting Guide


Step-by-Step DevOps Flow (ASCII Diagram)
------------------------------------------
Developer
   |
   |  git push (main branch)
   v
GitHub Repository
   |
   |  Triggers CI/CD Pipeline
   v
GitHub Actions
   |
   |  (runs on self-hosted runner)
   v
Self-Hosted Runner (Local Machine)
   |
   |-- docker build (backend)
   |-- docker build (frontend)
   |-- docker push (Docker Hub)
   |
   v
Docker Hub
   |
   |-- docker compose pull
   |-- docker compose up -d
   v
Docker Compose (Local Deployment)
   |
   |-- React Frontend (Port 5173)
   |-- Django Backend (Port 8000)

Step-by-Step DevOps Flow (ASCII Diagram)
-----------------------------------------

+-------------------+       HTTP API        +-------------------+
|                   |  ------------------> |                   |
|  React Frontend   |   http://backend:8000|  Django Backend   |
|  (Vite, Port 5173)|                      |  (Port 8000)      |
|                   |                      |                   |
+-------------------+                      +-------------------+
        |                                              |
        |------------ Docker Compose Network -----------|

PURPOSE OF THIS DOCUMENT

This document is written so that:

A new teammate can set up the project from scratch

A reviewer/interviewer can verify real DevOps work

The setup can be reproduced without asking questions

Every command used during the project journey is documented.

1️⃣ WHAT THIS PROJECT CONTAINS

Frontend: React (Vite)

Backend: Django

Containers: Docker & Docker Compose

CI/CD: GitHub Actions

Deployment: Local machine using a self-hosted GitHub Actions runner

2️⃣ PREREQUISITES (DO THIS FIRST)

Install these on your system:

Git

Docker Desktop

Docker Compose (comes with Docker Desktop)

GitHub account

Docker Hub account

Verify installation

Run each command and confirm it works:

git --version
docker --version
docker compose version


If any command fails, fix it before continuing.

3️⃣ CLONE THE PROJECT
git clone <repository-url>
cd devops-assessment

Verify structure

You must see:

backend/
frontend/
docker-compose.yml
.github/workflows/docker-ci-cd.yml
README.md
DEVOPS.md


If structure is different, stop and fix before proceeding.

4️⃣ RUN APPLICATION LOCALLY (DOCKER)
Step 1: Build images
docker compose build


👉 This builds frontend and backend images.

Step 2: Start containers
docker compose up -d

Step 3: Verify containers
docker ps


You should see both frontend and backend running.

Step 4: Access application

Frontend → http://localhost:5173

Backend → http://localhost:8000

Step 5: Stop containers (when needed)
docker compose down

5️⃣ HOW SERVICES COMMUNICATE (IMPORTANT)

Containers do not use localhost to talk to each other

Docker Compose provides internal DNS

Correct backend URL (used in frontend)
VITE_API_URL=http://backend:8000

6️⃣ CI/CD PIPELINE OVERVIEW
Trigger

Pipeline runs automatically on:

Every push to the main branch

Pipeline actions (in order)

Checkout repository code

Login to Docker Hub

Build backend Docker image

Push backend image

Build frontend Docker image

Push frontend image

Deploy locally using Docker Compose

7️⃣ GITHUB SECRETS (MANDATORY)

Add secrets at:

Repository → Settings → Secrets → Actions

Secret Name	What to put
DOCKER_USERNAME	Docker Hub username
DOCKER_PASSWORD	Docker Hub access token

⚠️ Do not use Docker Hub password. Use access token.

8️⃣ SELF-HOSTED RUNNER SETUP (WINDOWS)

This allows GitHub Actions to run jobs on the local machine.

Step 1: Go to runner page
Repository → Settings → Actions → Runners → New self-hosted runner


Choose:

OS: Windows

Architecture: x64

Step 2: Create runner directory
mkdir actions-runner
cd actions-runner

Step 3: Download runner

(Use the exact command shown by GitHub)

Invoke-WebRequest -Uri <runner-url> -OutFile runner.zip

Step 4: Extract runner
Add-Type -AssemblyName System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::ExtractToDirectory("runner.zip", "$PWD")

Step 5: Configure runner
./config.cmd --url https://github.com/<owner>/<repo> --token <TOKEN>


👉 When prompted:

Runner group → press Enter

Runner name → press Enter

Labels → press Enter

Work folder → press Enter

Run as service → Y

⚠️ Run PowerShell as Administrator for service setup.

Step 6: Verify runner

Go back to GitHub:

Settings → Actions → Runners


Status must show:

Self-hosted | Windows | Idle

9️⃣ DEPLOYMENT FLOW (AUTOMATIC)

When code is pushed to main:

GitHub Actions triggers workflow

Runner executes job locally

Images are pulled from Docker Hub

Containers restart automatically

Commands executed by CI:

docker compose pull
docker compose up -d

🔟 TROUBLESHOOTING (REAL ISSUES & FIXES)
Issue: Docker image pull failed
failed to resolve source metadata for docker.io


Fix

Restart Docker Desktop and retry

Issue: Frontend permission denied
EACCES: permission denied


Fix

RUN chown -R appuser:appgroup /app
USER appuser

Issue: Frontend cannot reach backend

Fix

VITE_API_URL=http://backend:8000

Issue: Django DisallowedHost

Fix

ALLOWED_HOSTS = ["localhost", "backend"]

Issue: CI failed with ||

Cause
Windows uses PowerShell, not Bash.

Fix

docker compose down
docker compose up -d

Issue: PowerShell blocked scripts

Fix

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

Issue: Runner offline / not configured

Fix

./config.cmd remove
./config.cmd --url <repo> --token <new-token>

11️⃣ QUICK START (NEW TEAMMATE)
git clone <repo>
cd devops-assessment
docker compose up -d


That’s it. CI/CD handles the rest.



AWS
-----

NOTE:
Ports 5173 and 8000 are exposed only for demonstration purposes.
In production, frontend should be served via port 80/443 and backend should remain private.

connect to ec2-instace by using powershell
-----------------------------------------
 ssh -i devops-assignment.pem ec2-user@35.154.58.195

 2️⃣ Update system packages
 sudo yum update -y

3️⃣ Install Docker
sudo yum install docker -y

 4️⃣ Start Docker service
sudo systemctl start docker

5️⃣ Enable Docker on boot
sudo systemctl enable docker

6️⃣ Add ec2-user to Docker group (VERY IMPORTANT)

Without this, you must use sudo every time.

sudo usermod -aG docker ec2-user

7️⃣ Logout & Login again (mandatory)
exit

8️⃣ Verify Docker installation
docker --version

🔐 Common Errors & Fixes (Interview Gold)
❌ permission denied while trying to connect to Docker daemon

✔ Fix:

sudo usermod -aG docker ec2-user
exit


Reconnect.

❌ docker: command not found

✔ Fix:

sudo yum install docker -y

❌ Docker not starting after reboot

✔ Fix:

sudo systemctl enable docker

🐳 Docker Compose Install & App Deployment on EC2 (Amazon Linux)
1️⃣ Confirm Docker is running
docker --version
sudo systemctl status docker

2️⃣ Install Docker Compose (v2 – recommended)
Download binary
sudo curl -L https://github.com/docker/compose/releases/download/v2.25.0/docker-compose-linux-x86_64 \
-o /usr/local/bin/docker-compose

Make it executable
sudo chmod +x /usr/local/bin/docker-compose

Verify
docker-compose version


✅ Install Git on EC2 (Amazon Linux)
1️⃣ Update package index
sudo yum update -y

2️⃣ Install Git
sudo yum install git -y

3️⃣ Verify Git installation
git --version

✅ Now clone your repository
git clone https://github.com/ranjan-fullstack/devops-assessment.git

Start containers:

docker compose up -d


Check status:

docker ps

🔥 FIX STEP 1: Check Docker is listening on ALL interfaces

Run this inside EC2:

docker ps


Then:

docker inspect react-frontend | grep HostPort -n


You should see something like:

"HostPort": "5173"


Now check binding:

ss -tulnp | grep 5173


✅ Expected output:

0.0.0.0:5173

✅ Step 1: Check backend container logs (MOST IMPORTANT)

Run this on EC2:

docker logs django-backend

🧹 IF YOU WANT CLEAN RESTART (SAFE)
docker compose down
docker compose build --no-cache
docker compose up -d

runner on ec2
------------
curl -o actions-runner-linux-x64-2.331.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.331.0/actions-runner-linux-x64-2.331.0.tar.gz

echo "5fcc01bd546ba5c3f1291c2803658ebd3cedb3836489eda3be357d41bfcf28a7  actions-runner-linux-x64-2.331.0.tar.gz" | sha256sum -c

tar xzf ./actions-runner-linux-x64-2.331.0.tar.gz


We will manually install the .NET runtime dependencies required by GitHub Actions runner.

🔧 Step 1: Install required libraries

Run all commands below on EC2:

sudo dnf install -y \
  libicu \
  openssl \
  krb5-libs \
  zlib \
  libgcc \
  libstdc++ \
  lttng-ust


These are exactly what the runner needs.

🔧 Step 2: Verify libicu is installed
rpm -qa | grep libicu

# Create the runner and start the configuration experience
$ ./config.sh --url https://github.com/ranjan-fullstack/devops-assessment --token B2HHYK6JVTTLP3TSZ4HZP7TJO6KHI

for running runner
------------------
./run.sh

Interview-ready summary (USE THIS)
-----------------------------------

I implemented a CI/CD pipeline using GitHub Actions with a self-hosted runner on AWS EC2.
On every push to main, Docker images are built, pushed to Docker Hub, and deployed automatically using Docker Compose on EC2


full automate build process
-----------------------------

Developer Pushes Code
        ↓
GitHub Actions (CI)
 - Checkout
 - Build
 - Test
 - Docker Build
        ↓
Trigger Jenkins Job
        ↓
Jenkins Pipeline
 - SonarQube Scan
 - Trivy Scan
 - Approval (optional)
 - Deploy to EC2 / EKS


jenkin download on ec2
----------------------
sudo yum update -y
sudo yum install java-17-amazon-corretto -y
sudo wget -O /etc/yum.repos.d/jenkins.repo \
https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
sudo yum install jenkins -y
sudo systemctl start jenkins
sudo systemctl enable jenkins

passwod -   sudo cat /var/lib/jenkins/secrets/initialAdminPassword

❌ Why Built-In Node is OFFLINE

From your screenshot (red message 👇):

Disk space is below threshold of 1.00 GiB
Only 453 MB left on /tmp

Jenkins rule:

👉 If /tmp free space < 1 GB, Jenkins automatically marks node OFFLINE
This is default safety behavior in real companies.