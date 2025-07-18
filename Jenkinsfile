pipeline {
        agent {
        label 'agent-1'
    }

    environment {
        // AWS_REGION = 'eu-west-1'
        IMAGE_NAME = 'cicd-jenkins-demo'
    }

    stages {
        stage('Pip3 test + create env') {
            steps {
                sh '''
                    pip3 --version
                    python3 -m pip3 install --user virtualenv
                    python3 -m virtualenv venv
                    . venv/bin/activate
                    '''
                
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python3 -m pip3 install -r requirements.txt'
                sh 'mkdir -p reports'
                sh 'PYTHONPATH=testy pytest testy --junitxml=reports/pytest.xml'
                junit 'reports/pytest.xml'
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}")
                }
            }
        }

        /*
        stage('Push to ECR') {
            steps {
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'aws-credentials'
                ]]) {
                    script {
                        def accountId = sh(
                          script: "aws sts get-caller-identity --query Account --output text",
                          returnStdout: true
                        ).trim()

                        sh """
                        aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${accountId}.dkr.ecr.${AWS_REGION}.amazonaws.com

                        docker tag ${IMAGE_NAME}:latest ${accountId}.dkr.ecr.${AWS_REGION}.amazonaws.com/${IMAGE_NAME}:latest

                        docker push ${accountId}.dkr.ecr.${AWS_REGION}.amazonaws.com/${IMAGE_NAME}:latest
                        """
                    }
                }
            }
        }
        */

        /*
        stage('Deploy to ECS') {
            steps {
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'aws-credentials'
                ]]) {
                    sh '''
                        aws ecs update-service \
                          --cluster CICD-Cluster \
                          --service my-service \
                          --force-new-deployment \
                          --region eu-west-1
                    '''
                }
            }
        }
        */
    }
}
