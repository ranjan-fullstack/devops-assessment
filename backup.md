name: CI/CD Pipeline - Docker Build, Push & EC2 Deploy

on:
  push:
    branches:
      - main

jobs:
  build-push-deploy:
    # 🔥 Runs on EC2 self-hosted Linux runner
    runs-on: self-hosted

    steps:
      # 1️⃣ Checkout source code
      - name: Checkout code
        uses: actions/checkout@v4

      # 2️⃣ Login to Docker Hub (secure)
      - name: Login to Docker Hub
        run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin

      # 3️⃣ Build & Push Django Backend Image
      - name: Build & Push Backend Image
        run: |
          docker build -t ${{ secrets.DOCKER_USERNAME }}/django-backend:latest ./backend
          docker push ${{ secrets.DOCKER_USERNAME }}/django-backend:latest

      # 4️⃣ Build & Push React Frontend Image
      - name: Build & Push Frontend Image
        run: |
          docker build -t ${{ secrets.DOCKER_USERNAME }}/react-frontend:latest ./frontend
          docker push ${{ secrets.DOCKER_USERNAME }}/react-frontend:latest

      # 5️⃣ Deploy on EC2 using Docker Compose
      - name: Deploy using Docker Compose
        run: |
          docker compose down || true
          docker compose pull
          docker compose up -d
