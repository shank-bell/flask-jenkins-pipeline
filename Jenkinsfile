pipeline {
    agent any

    environment {
        DEPLOY_DIR = 'deploy'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate.bat
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                bat '''
                    call venv\\Scripts\\activate.bat
                    python -m unittest discover -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Copying application to deployment directory...'
                bat '''
                    if not exist "%DEPLOY_DIR%" mkdir "%DEPLOY_DIR%"
                    copy /Y app.py "%DEPLOY_DIR%\\"
                    copy /Y requirements.txt "%DEPLOY_DIR%\\"
                    dir "%DEPLOY_DIR%"
                '''
            }
        }
    }

    post {
        success { echo 'Pipeline succeeded - app deployed to workspace/deploy' }
        failure { echo 'Pipeline FAILED - see stage results above' }
    }
}
