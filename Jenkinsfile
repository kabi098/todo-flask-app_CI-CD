pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/kabi098/todo-flask-app_CI-CD.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest test_app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-cicd-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop flask-cicd-app || true
                docker rm flask-cicd-app || true
                docker run -d -p 5000:5000 --name flask-cicd-app flask-cicd-app
                '''
            }
        }

        stage('Test Endpoint') {
            steps {
                sh 'curl http://localhost:5000/hello'
            }
        }
    }
}