pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {
        stage('Install Python') {
            steps {
                sh '''
                    python3 -m venv $VENV
                    . $VENV/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
            echo 'Running Tests'
            script {
            env.testResults = sh(returnStatus: true, script: 'pytest')
        }
            }
            steps {
            echo 'Running Pytest'
            sh '''
                    pytest
                '''
            
        }
            }
        }
        stage('Deploy') {
            steps {
            echo 'Deploying app...'
            script {
            if (env.testResults == 0) {
                echo 'Test passed'
            } else {
                echo 'Test failed'
            }
        }
            }
        }
    }
}