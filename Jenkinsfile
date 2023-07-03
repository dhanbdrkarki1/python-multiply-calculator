pipeline {
  agent any 
  stages {
    stage ('Checkout'){
        steps{
            git branch: 'main', url: 'https://github.com/dhanbdrkarki1/python-multiply-calculator.git'
        }
    }
    stage ('Unit Test'){
        steps{
            sh "python3 test_calculator.py"
        }
    }
  }
  post {
    success {
        echo "Tested successfully!"
    }
  }
}