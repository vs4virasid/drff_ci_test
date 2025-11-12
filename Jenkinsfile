pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

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
                bat '''
                echo Running Django tests with pytest...
                venv\\Scripts\\pytest --ds=drff_ci_test.settings --maxfail=1 --disable-warnings -v
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Build passed '
            githubNotify context: 'CI', status: 'SUCCESS', description: 'Build passed successfully', targetUrl: env.BUILD_URL
        }
        failure {
            echo '❌ Build failed'
            githubNotify context: 'CI', status: 'FAILURE', description: 'Build failed', targetUrl: env.BUILD_URL
        }
    }
}
