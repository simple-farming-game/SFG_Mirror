pipeline {
    agent any   // Jenkins가 어떤 컴퓨터에서 일을 할지 정하는 부분
    stages {
        stage('Gitea Clone') {   // 프로그램을 빌드하는 단계
            steps {
                git branch: 'rewrite',
                    url: 'https://gitea.sinoka.dev/sinoka/simple_farming_game'
            }
        }
        stage('Build') {   // 프로그램을 빌드하는 단계
            steps {
                timeout(time: 10, unit: 'MINUTES') {
                    sh 'go mod tidy'
                }
                sh 'go build main.go'   // go라는 언어로 프로그램을 빌드해라
            }
        }
    }
}
