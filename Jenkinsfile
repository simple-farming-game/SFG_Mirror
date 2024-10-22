pipeline {
    agent any

    environment {
        GO_VERSION = '1.22.8' // Specify your Go version
        GOBIN = "/usr/local/go/bin" // Set the GOBIN
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from Gitea
                git url: 'https://gitea.sinoka.dev/sinoka/simple_farming_game', branch: 'rewrite'
            }
        }

        stage('Set up Go Environment') {
            steps {
                // Install Go if it's not already installed
                script {
                    sh """
                    curl -OL https://golang.org/dl/go${GO_VERSION}.linux-arm64.tar.gz
                    sudo tar -C /usr/local -xzf go${GO_VERSION}.linux-arm64.tar.gz
                    """
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    // Set up Go environment variables
                    env.PATH = "${GOBIN}:${env.PATH}"
                    sh 'go mod tidy' // Ensure dependencies are up to date
                    sh 'go get ./...' // Build the Go application
                    sh 'go build -o SFG ./...' // Build the Go application
                }
            }
        }
}
}