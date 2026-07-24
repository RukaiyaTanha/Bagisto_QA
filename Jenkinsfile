pipeline {
    agent any

    environment {
        BASE_URL = 'http://127.0.0.1:8000'
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Pulling latest code from GitHub...'
                git branch: 'main',
                    url: 'https://github.com/RukaiyaTanha/Bagisto_QA.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python libraries...'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo 'Running all Pytest tests...'
                bat 'pytest tests/ --html=report.html --self-contained-html -v'
            }
        }

        stage('Publish Test Report') {
            steps {
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Bagisto SQA Test Report'
                ])
            }
        }
    }

    post {
        success {
            echo 'ALL TESTS PASSED!'
        }
        failure {
            echo 'TESTS FAILED — Check report above!'
        }
        always {
            echo 'Pipeline finished.'
        }
    }
}