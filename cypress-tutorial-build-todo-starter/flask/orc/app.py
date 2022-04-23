import os
import docker
from flask import Flask, Response
import xml.etree.ElementTree as ET
app = Flask(__name__)

@app.route("/run-cypress")
def run_cypress():
    client = docker.from_env()
    client.containers.run("cypress-cypress-1")

@app.route("/")
def home():
    client = docker.from_env()
    print(client.containers.list())
    return "HELLO!"

@app.route("/results")
def res():
    longlist = ""
    metric_name = "test"
    for file in os.listdir("/code/results/"):
        tree = ET.parse("/code/results/" + file)
        root = tree.getroot()
        for child in root:
            test_runtime = metric_name  + "_runtime" + "{name=\"" + str(child.attrib["name"]) + "\", timestamp=\"" + str(
                child.attrib["timestamp"]) + "\"} " + str(child.attrib["time"]) + "\n"
            test_failures = metric_name  + "_failure" + "{name=\"" + str(child.attrib["name"]) + "\", timestamp=\"" + str(
                child.attrib["timestamp"]) + "\"} " + str(child.attrib["failures"]) + "\n"
            longlist = longlist + test_runtime + test_failures
    return Response(longlist, mimetype='text/plain')


if __name__ == "__main__":
    app.run()
