✅ STEP 1: RUN SONARQUBE ON EC2 (Docker)

On your Jenkins EC2:

docker run -d \
  --name sonarqube \
  -p 9000:9000 \
  sonarqube:lts

  ⏳ Wait 2–3 minutes
Open in browser:

http://<EC2_PUBLIC_IP>:9000

🔐 Default Login
username: admin
password: admin


✅ STEP 1: Create Project (Manual)

Click Manually

Fill like this:

Project display name:

devops-assessment


Project key (important, no spaces):

devops-assessment


Click Set up


👉 Click: “With Jenkins” ✅

(Do NOT click GitHub Actions here because your scan runs inside Jenkins.)

✅ Step 1: Select DevOps platform

On this screen:

👉 Click GitHub

✅ STEP 1: Install required Jenkins plugins

Go to Jenkins → Manage Jenkins → Plugins → Available

Install these (VERY IMPORTANT):

✔️ SonarQube Scanner for Jenkins
✔️ Pipeline: Stage View (optional but good)
✔️ Credentials Binding (usually already there)

👉 After install → Restart Jenkins (safe restart)



✅ STEP 1 (MANDATORY): Restart Jenkins

You can see this line 👇

“Downloaded Successfully. Will be activated during the next boot”

👉 Restart Jenkins now

Do one of these:

Click “Restart Jenkins when installation is complete”, OR

Open:

http://13.233.67.237:8080/restart


⚠️ Without restart → SonarQube plugin will NOT work.

✅ STEP 2: Create SonarQube Token (VERY IMPORTANT)
In SonarQube (port 9000)

Top-right avatar → My Account

Security

Generate token:

Name: jenkins-sonar

Type: Global

COPY the token (only shown once)

✅ STEP 3: Add Sonar Token in Jenkins Credentials

Go to:

Jenkins → Manage Jenkins → Credentials → Global → Add Credentials

Kind: Secret Text

Secret: 👉 paste Sonar token

ID:

sonar-token


Description: SonarQube Token

Save 💾

✅ STEP 4: Configure SonarQube Server in Jenkins

Go to:

Manage Jenkins → System

🔹 SonarQube Servers

✔️ Enable injection

Name:

sonarqube


Server URL:

http://13.233.67.237:9000


Server authentication token:

sonar-token


Save 💾

✅ STEP 5: Configure Sonar Scanner Tool

Manage Jenkins → Tools

SonarQube Scanner

Name:

sonar-scanner


✔️ Install automatically

Version: latest

Save 💾

✅ STEP 6: Add SonarQube stages to Jenkinsfile

👉 Add this BEFORE Docker build stages

stage('SonarQube Scan') {
    steps {
        withSonarQubeEnv('sonarqube') {
            sh '''
              sonar-scanner \
              -Dsonar.projectKey=devops-assessment \
              -Dsonar.sources=backend,frontend \
              -Dsonar.sourceEncoding=UTF-8
            '''
        }
    }
}

stage('Quality Gate') {
    steps {
        timeout(time: 2, unit: 'MINUTES') {
            waitForQualityGate abortPipeline: true
        }
    }
}


🔥 This makes your pipeline SECURITY-GATED (real DevSecOps).

✅ STEP 7: Run Jenkins Job

Expected result:

✔️ Sonar scan logs in Jenkins

✔️ Project updated in SonarQube dashboard

✔️ Quality Gate result shown

❌ Pipeline FAILS if code quality is bad (this is GOOD)



“We integrated SonarQube into Jenkins to enforce quality gates before Docker image creation.
If the quality gate fails, the pipeline stops automatically, preventing insecure code from reaching production.”