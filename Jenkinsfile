pipeline{
    
    agent { label 'dev'}
    stages{
        stage("Code"){
            steps{
                git url: "https://github.com/DasShiv-3108/simple-flask-input-app.git", branch: "master"
            }
        }
        stage("Build"){
            steps{
                sh "docker build -t simple-flask-input-app ."
            }
        }
        stage("Test"){
            steps{
                echo "Test Done"
            }
        }
        stage("Push To D_Hub"){
            steps{
                withCredentials([usernamePassword(
                    credentialsId:"DockerHubCreds",
                    usernameVariable: "DockerUser",
                    passwordVariable: "DockerPass"
                )]){
                    sh '''
                    echo "$DockerPass" | docker login -u "$DockerUser" --password-stdin
                    
                    docker tag simple-flask-input-app \
                    "$DockerUser/simple-flask-input-app"
                    
                    docker push \
                    "$DockerUser/simple-flask-input-app:latest"
                    
                    '''
                }
                
            }
        }
        stage("Deploy"){
            steps{
                sh "docker compose up -d --build"
            }
        }
    }
post {
    success {
        emailext body: 'Build Success',
            subject: 'Jenkins Build successfuly',
            to: 'dasshiv3108@gmail.com'
    }
    failure {
         emailext body: 'Build failed',
             subject: 'Jenkins Build Failed',
             to: 'dasshiv3108@gmail.com'
    }
}
}
