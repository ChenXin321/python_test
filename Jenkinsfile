pipeline{
    agent any
    stages{
        stage("test"){
            when{
                branch "pro"
            }
            steps{
                echo "yes pro"
            }
        }
    }
      post {
        always {
            echo 'One way or another, I have finished'
        }
        success {
            echo "success"
        }
        unstable {
            echo 'I am unstable :/'
        }
        failure {
            echo 'I failed :('
        }
        changed {
            echo 'Things were different before...'
        }
    }
}
