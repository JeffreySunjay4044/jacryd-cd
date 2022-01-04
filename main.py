# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import subprocess

from flask import Flask, request
from flask import json

app = Flask(__name__)

@app.route('/executeDeploy', methods=['GET'])
def executeScript():
    """
    This API fetches the list of all namespaces in the cluster along with its age
    :return HTTP Response with list of all-namespaces in the cluster:
    """
    data = request.data
    repositoryUrl = data.repositoryUrl
    scriptLocation = data.scriptLocation
    credentials = data.credentials
    if credentials is not None:
        MONGO_CREDS = credentials.mongo_creds
        REDIS_PWD = credentials.redis_creds
        OSM_CMDB_URL = credentials.dsm_cmdb_url
        DOPPLER_TOKEN = credentials.doppler_token
        subprocess.Popen(['./execute-deploy.sh %s %s %s' % (repositoryUrl, scriptLocation)], shell=True)
    return app.response_class(response=json.dumps({"status": "Success"}), status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
