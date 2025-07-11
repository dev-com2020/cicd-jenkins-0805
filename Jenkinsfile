pipeline {
    agent any

    environment {
        AWS_REGION = 'eu-west-1'
        IMAGE_NAME = 'cicd-jenkins-demo'
        AWS_ACCOUNT_ID = 'aws-credentials'
    }

    stages {
        stage('Build Docker image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}")
                }
            }
        }

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



        stage('Deploy to ECS') {
            steps {
                sh 'aws ecs update-service --cluster CICD-Cluster --service my-service --force-new-deployment --region eu-central-1'
            }
        }
    }
}
