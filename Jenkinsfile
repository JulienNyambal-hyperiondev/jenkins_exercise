pipeline {
    agent any
    triggers {
        pollSCM '* * * * *'
    }
    stages {
	    stage('Lib Intallation') {
            steps {
                echo "Virtual Environment.."
                sh '''
				cd my_calculator
                python3 -m venv jenkins_venv
				. ./jenkins_venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."

                sh '''
                cd my_calculator
                . ./jenkins_venv/bin/activate
                python3 -m pytest -v
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}