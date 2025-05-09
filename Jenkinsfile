pipeline {
    agent any
    stages {
        stage('Install Python') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        def testResults
        stage('Test') {
            steps {
            echo 'Running Tests'
            testResults = sh(returnStatus: true, script: 'mvn test')
        }
        }
        stage('Deploy') {
            steps {
            echo 'Deploying app...'
            if (testResults == 0) {
                echo 'Test passed'
            } else {
                echo 'Test failed'
            }
        }
        }
    }
}