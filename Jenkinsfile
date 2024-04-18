pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/Okios2/PyTest-Tetris-Fork-.git'
        GIT_CRED_ID = 'c22155b7-9e75-4f1c-bf10-f5be9ada6241'
        GIT_BRANCH = 'master'
    }
    
    triggers {
        pollSCM('* * * * *')
    }
    
    stages {
        stage('Collect') {
            steps {
                git branch: "${GIT_BRANCH}", credentialsId: "${GIT_CRED_ID}", url: "${GIT_REPO}"
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building..'
                sh ''' 
                ls
                docker build -t tetrisbuild:latest -f ./Dockerfiles/Dockerfile .
                docker run --name tetrisbuild -v ./artifacts:/dist tetrisbuild:latest
                docker logs tetrisbuild > ./log/log_builder.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh '''
                docker build -t tetristest:latest -f ./Dockerfiles/DockerfileTest .
                docker logs tetristest > ./log/log_tester.txt
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying..'
                sh '''
                docker build -t tetrisdeploy:latest -f ./Dockerfiles/DockerfileDeploy .
                docker logs tetrisdeploy > ./log/log_deploy.txt
                '''
            }
        }

        stage('Publish') {
            steps {
                echo 'Publishing..'
                sh '''

                '''
            }
        }  
    }
}