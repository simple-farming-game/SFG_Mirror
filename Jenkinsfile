pipeline {
    agent any   // Jenkins가 어떤 컴퓨터에서 일을 할지 정하는 부분
    stages {
        stage('빌드') {   // 프로그램을 빌드하는 단계
            steps {
                sh 'go build'   // go라는 언어로 프로그램을 빌드해라
            }
        }
        stage('배포') {   // 프로그램을 서버에 배포하는 단계
            steps {
                sh 'scp myapp user@server:/path/to/deploy'  // 프로그램을 서버에 복사해서 배포해라
            }
        }
    }
}
