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
    longlist = list()
    for file in os.listdir('./results/'):
        tree = ET.parse(file)
        root = tree.getroot()
        for child in root:
            c = str(child.tag) + str(child.attrib)
            longlist.append(c)
            for grandchild in child:
                c = str(grandchild.tag) + str(grandchild.attrib)
                longlist.append(c)
    return longlist


if __name__ == "__main__":
    app.run()
