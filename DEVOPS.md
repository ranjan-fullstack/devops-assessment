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