pipeline {
    agent any
    environment {
                 MONGO_CREDS = credentials('MONGO')
                 REDIS_PWD = credentials('REDIS')
                 OSM_CMDB_URL = 'https://optimaltest.service-now.com/api'
                 DOPPLER_TOKEN= credentials ('DOPPLER_TOKEN')
    }
    stages {

            stage('Trigger build step'){
                steps {
                       dir ('/var/lib/jenkins/workspace/new-node-test/lc-client'){
                       sh 'curl --location --request GET "localhost:5000/executeDeploy" \ --header "Content-Type: application/json" \ --data-raw \"{ "repositoryUrl": "", "scriptLocation": "", "credentials": { "mongo_creds": "", "redis_creds": "", "dsm_cmdb_url": "", "doppler_token": "" } }'
                       }
                }
            }
}