node {
    checkout scm
    withEnv(['DISABLE_AUTH=true',
             'DB_ENGINE=sqlite']){
             stage('Build') {
                echo "build 123"
                sh 'printenv'
             }
    }

}