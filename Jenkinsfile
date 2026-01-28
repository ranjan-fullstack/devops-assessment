pipeline {
    agent any

    environment {
        BACKEND_IMAGE  = "backend-app"
        FRONTEND_IMAGE = "frontend-app"
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

        stage('Verify Images') {
            steps {
                sh '''
                  docker images | grep backend-app
                  docker images | grep frontend-app
                '''
            }
        }
    }
}
