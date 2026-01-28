pipeline {
    agent any

    environment {
        IMAGE_NAME = "jenkins-demo-app"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                  docker build -t $IMAGE_NAME:latest .
                '''
            }
        }

        stage('Docker Verify') {
            steps {
                sh '''
                  docker images | grep $IMAGE_NAME
                '''
            }
        }
    }
}
