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
        emailtext(
            subject: "Build Successfull",
            body: "Good news: Your build was successfull",
            to: 'dasshiv3108@gmail.com'
            )
    }
    failure {
        emailtext(
            subject: "Build failed",
            body: "Bad NEWS: Build failed"
            to: 'dasshiv3108@gmail.com'
            )
    }
}
}
