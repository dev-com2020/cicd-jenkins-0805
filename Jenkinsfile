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
                script {
                    echo 'Running Pytest...'
                    // Zmienna Groovy, NIE env!
                    testResults = sh(returnStatus: true, script: '''
                        . venv/bin/activate
                        pytest
                    ''')
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying app...'
                    if (testResults == 0) {
                        echo '✅ Test passed – deployment continues.'
                    } else {
                        echo '❌ Test failed – skipping deployment.'
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }
    }
}
