pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/kabi098/todo-flask-app_CI-CD.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-cicd-app .'
            }
        }

        stage('Run Tests inside Docker') {
            steps {
                sh '''
                docker run --rm flask-cicd-app python -m unittest test_app.py
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                echo "Cleaning old container..."
                docker rm -f flask-cicd-app || true

                echo "Starting new container..."
                docker run -d -p 5000:5000 --name flask-cicd-app flask-cicd-app
                '''
            }
        }

        stage('Test Endpoint') {
            steps {
                sh '''
                echo "Waiting for app to start..."
                sleep 5

                echo "Testing endpoint inside container..."
                docker exec flask-cicd-app curl http://localhost:5000/hello
                '''
            }
        }
    }
}