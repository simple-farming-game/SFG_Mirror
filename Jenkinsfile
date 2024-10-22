pipeline {
    agent none

    environment {
        GO_VERSION = '1.22.8' // 사용할 Go 버전
        GOBIN = "/usr/local/go/bin" // GOBIN 설정
    }

    stages {
        stage('Checkout') {
            steps {
                // Gitea에서 코드 체크아웃
                git url: 'https://gitea.sinoka.dev/sinoka/simple_farming_game', branch: 'rewrite'
            }
        }

        stage('Set up Go Environment') {
            steps {
                script {
                    // Go가 설치되어 있는지 확인
                    def goInstalled = sh(script: 'go version', returnStatus: true)
                    if (goInstalled != 0) {
                        // Go가 설치되어 있지 않으면 설치
                        sh "curl -OL https://golang.org/dl/go${GO_VERSION}.linux-arm64.tar.gz"
                        sh "sudo tar -C /usr/local -xzf go${GO_VERSION}.linux-arm64.tar.gz"
                    } else {
                        echo 'Go is already installed.'
                    }
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    // Go 환경 변수를 설정
                    env.PATH = "${GOBIN}:${env.PATH}"
                    sh 'go mod tidy' // 의존성 정리
                    sh 'go get ./...' // 의존성 가져오기
                    sh 'go build -o SFG ./...' // Go 애플리케이션 빌드
                }
            }
        }

        // 추가적인 배포 단계
        stage('Deploy') {
            steps {
                script {
                    // Jenkins 서버에 애플리케이션을 배포 (예: 특정 디렉토리로 복사)
                    sh 'cp SFG /path/to/deploy/' // 실제 배포 경로로 수정 필요
                    // 또는 실행할 경우
                    // sh './SFG' // 애플리케이션 실행
                }
            }
        }
    }
}