import os
import docker
from flask import Flask
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
    metric_name = "test_"
    index = 1
    for file in os.listdir(".\\results\\"):
        tree = ET.parse(".\\results\\" + file)
        root = tree.getroot()
        for child in root:
            c = metric_name + str(index) + "{name=\"" + str(child.attrib["name"]) + "\", timestamp=\"" + str(
                child.attrib["timestamp"]) + "\", tests=\"" + str(child.attrib["tests"]) + "\", time=\"" + str(
                child.attrib["time"])+ "\", failures=\"" + str(child.attrib["failures"]) + "\"}"
            index = index + 1
            longlist = longlist + c
    return longlist


if __name__ == "__main__":
    app.run()
