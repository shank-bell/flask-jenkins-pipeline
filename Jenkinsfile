pipeline {
    agent any

    environment {
        DEPLOY_DIR = "${WORKSPACE}/deploy"
    }

    stages {
        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    . venv/bin/activate
                    python -m unittest discover -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Copying application to deployment directory...'
                sh '''
                    mkdir -p "$DEPLOY_DIR"
                    cp app.py requirements.txt "$DEPLOY_DIR/"
                    ls -l "$DEPLOY_DIR"
                '''
            }
        }
    }

    post {
        success { echo 'Pipeline succeeded - app deployed to workspace/deploy' }
        failure { echo 'Pipeline FAILED - see stage results above' }
    }
}
