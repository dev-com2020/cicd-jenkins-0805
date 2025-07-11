pipeline {
    agent any

    environment {
        AWS_REGION = 'eu-central-1'
        IMAGE_NAME = 'cicd-jenkins-demo'
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'github-token', url: 'https://github.com/dev-com2020/cicd-jenkins-0805.git'
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Push to ECR') {
            environment {
                AWS_ACCOUNT_ID = credentials('aws-credentials') // lub wpisz ręcznie
            }
            steps {
                script {
                    sh """
                    aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
                    docker tag ${IMAGE_NAME}:latest ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${IMAGE_NAME}:latest
                    docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${IMAGE_NAME}:latest
                    """
                }
            }
        }

        stage('Deploy to ECS') {
            steps {
                sh 'aws ecs update-service --cluster CICD-Cluster --service my-service --force-new-deployment --region eu-central-1'
            }
        }
    }
}
