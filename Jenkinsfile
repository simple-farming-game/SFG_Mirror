pipeline {
    agent none

    environment {
        GO_VERSION = '1.22.8' // 사용할 Go 버전
        GOBIN = "/usr/local/go/bin" // GOBIN 설정
        PATH = "${GOBIN}:${env.PATH}"
    }

    stages {
        stage('Setup') {
            agent any
            steps {
                script {
                    sh "go env -w \"CGO_ENABLED=1\""
                }
            }
            
        }
        stage('Checkout') {
            agent any
            steps {
                // Gitea에서 코드 체크아웃
                git url: 'https://gitea.sinoka.dev/sinoka/simple_farming_game', branch: 'rewrite'
            }
        }

        stage('Set up Go Environment') {
            agent any
            steps {
                script {
                    // Go가 설치되어 있는지 확인
                    def goInstalled = sh(script: 'go version', returnStatus: true)
                    if (goInstalled != 0) {
                        // Go가 설치되어 있지 않으면 설치
                        sh "curl -OL https://golang.org/dl/go${GO_VERSION}.linux-amd64.tar.gz" // 아키텍처 확인
                        sh "sudo tar -C /usr/local -xzf go${GO_VERSION}.linux-amd64.tar.gz"
                    } else {
                        echo 'Go is already installed.'
                    }
                    // Go 환경 변수를 설정
                    env.PATH = "${GOBIN}:${env.PATH}"
                }
            }
        }

        stage('Build') {
            agent any
            steps {
                script {
                    sh 'pwd'
                    sh 'go mod tidy' // 의존성 정리
                    sh 'go get ./...' // 의존성 가져오기
                    sh 'go build -o ./build/SFG ' // Go 애플리케이션 빌드
                    sh 'echo "chmod +x ./SFG" > ./build/run.sh'
                    sh 'echo "./SFG" >> ./build/run.sh'
                    buildResult = hudson.model.Result.SUCCESS.toString()
                }
            }
        }

        stage('Archive Artifact') {
            agent any
            steps {
                script {
                    dir('./') {
                        try {
                            echo '==== archive artifact start ===='
                            sh 'tar -czvf build.tar.gz build'
                            archiveArtifacts artifacts: 'build.tar.gz', fingerprint: true
                            echo '==== archive artifact done ===='
                        } catch (Exception e) {

                        }
                    }
                }
            }
        }
    }
}
