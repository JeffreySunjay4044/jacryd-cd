# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import subprocess

from flask import Flask, request
from flask import json

app = Flask(__name__)

@app.route('/executeDeploy/<reposit>', methods=['GET'])
def executeScript():
    """
    This API fetches the list of all namespaces in the cluster along with its age
    :return HTTP Response with list of all-namespaces in the cluster:
    """
    data = request.data
    repositoryUrl = data.repositoryUrl
    scriptLocation = data.scriptLocation
    imageId = data.imageId
    subprocess.Popen(['./execute-deploy.sh %s %s %s' % (repositoryUrl, scriptLocation, imageId)], shell=True)
    return app.response_class(response=json.dumps({"status": "Success"}), status=200, mimetype='application/json')



if __name__ == '__main__':
    app.run(host='0.0.0.0')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
