pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t studexis-core .'
      }
    }
    stage('Test') {
      steps {
        sh 'pip install pytest && pytest tests'
      }
    }
    stage('Code Quality') {
      steps {
        echo 'Run SonarCloud scan here (setup required)'
      }
    }
    stage('Security') {
      steps {
        sh 'pip install bandit && bandit app.py'
      }
    }
    stage('Deploy') {
      steps {
        sh 'docker run -d -p 5000:5000 --name studexis-api studexis-core || true'
      }
    }
    stage('Release') {
      steps {
        sh 'echo "Tagging release v1.0"'
      }
    }
    stage('Monitoring') {
      steps {
        sh 'curl -s http://localhost:5000/health || echo "App is down"'
      }
    }
  }
}
