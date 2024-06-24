pipeline {
    agent any 
        environment {
            AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
            AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
        }
    stages {
        stage ('Install Dependencies') {
            steps {
                script {
                    bat 'python -m pip install boto3'
                    bat 'python -m pip install awswrangler'
                }
            }
        }
        stage("Run the code") {
            steps {
                bat 'python aws_wrangler_test.py'
            }
        }
    }
}