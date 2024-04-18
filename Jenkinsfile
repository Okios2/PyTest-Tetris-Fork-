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
                sh '''
                    chmod +x clear.sh
                    ./clear.sh
                '''
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building..'
                sh ''' 
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
                docker run --name tetristest -v ./artifacts:/dist tetristest:latest
                docker logs tetristest > ./log/log_tester.txt
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying..'
                sh '''
                docker build -t tetrisdeploy:latest -f ./Dockerfiles/DockerfileDeploy .
                docker run --name tetrisdeploy -v ./artifacts:/dist tetrisdeploy:latest
                docker logs tetrisdeploy > ./log/log_deploy.txt
                '''
            }
        }

        stage('Publish') {
            steps {
                echo 'Publishing..'
                withCredentials([usernamePassword(credentialsId: 'Docker-Hub-Credentials', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
                sh '''
                docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}
                docker build -t tetrisSatyammittal:latest -f ./Dockerfiles/Dockerfile .
                docker tag okios/tetrisSatyammittal:latest okios/tetrisSatyammittal:1.0.0
                docker push okios/tetrisSatyammittal:1.0.0
                '''
            }
        }  
    }
}
