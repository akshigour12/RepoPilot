pipeline {
    agent any

    triggers {
        githubPush()
    }

    environment {
        VENV = "venv"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv ${VENV}
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Verify Application') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    python -m py_compile app.py
                    python -m py_compile github_client.py
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . ${VENV}/bin/activate

                    if [ -d tests ]; then
                        pytest
                    else
                        echo "No tests found. Skipping..."
                    fi
                '''
            }
        }

    }

    post {

        success {
            emailext(
                subject: "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
Job : ${env.JOB_NAME}

Build : ${env.BUILD_NUMBER}

Status : SUCCESS

URL : ${env.BUILD_URL}
""",
                to: "akshigour12@gmail.com"
            )
        }

        failure {
            emailext(
                subject: "FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
Job : ${env.JOB_NAME}

Build : ${env.BUILD_NUMBER}

Status : FAILED

URL : ${env.BUILD_URL}
""",
                to: "akshigour12@gmail.com"
            )
        }
    }
}
