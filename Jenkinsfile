pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                bat '''
                python -m venv venv
                venv\\Scripts\\pip install --upgrade pip
                venv\\Scripts\\pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\pytest app'
            }
        }
    }
}
