pipeline {
    agent any

    environment {
        DOCKERHUB_USER = "rkdocker7894"
        BACKEND_IMAGE  = "django-backend"
        FRONTEND_IMAGE = "react-frontend"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Backend Image') {
            steps {
                sh '''
                  docker build -t $BACKEND_IMAGE:latest ./backend
                '''
            }
        }

        stage('Build Frontend Image') {
            steps {
                sh '''
                  docker build -t $FRONTEND_IMAGE:latest ./frontend
                '''
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                      echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    '''
                }
            }
        }

        stage('Tag & Push Images') {
            steps {
                sh '''
                  docker tag $BACKEND_IMAGE:latest $DOCKERHUB_USER/$BACKEND_IMAGE:latest
                  docker tag $FRONTEND_IMAGE:latest $DOCKERHUB_USER/$FRONTEND_IMAGE:latest

                  docker push $DOCKERHUB_USER/$BACKEND_IMAGE:latest
                  docker push $DOCKERHUB_USER/$FRONTEND_IMAGE:latest
                '''
            }
        }

      stage('Deploy on EC2 using Docker Compose') {
           steps {
                sh '''
                  echo "🚀 Deploying on EC2..."

                  docker-compose down || true
                  docker-compose pull
                  docker-compose up -d --remove-orphans

                  docker ps
                '''
            }
        }

    }

    post {
        always {
            sh 'docker logout'
        }
        success {
            echo "✅ Application deployed successfully on EC2"
        }
        failure {
            echo "❌ Deployment failed"
        }
    }
}
