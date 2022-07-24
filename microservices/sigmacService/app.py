import base64
from flask import Flask, jsonify, request
import subprocess
import os
import subprocess
import configparser
import json


app = Flask(__name__)
Config = configparser.ConfigParser()
configFilePath = './microservices/sigmacService/config.ini'
Config.read(configFilePath)

@app.route("/lists")
def get_list():
    os.chdir( Config.get('Paths', 'Tools'))

    target = '--lists'
    sigmac = "python3 sigmac {}".format(target)
    return subprocess.getoutput(sigmac) #sigmac --lists

#todo: prerobit podla https://github.com/SigmaHQ/sigma/blob/b1c1650897c0a1006ac96ee0f5e959346fac1698/tools/sigma/backends/discovery.py#L28
@app.route("/backends")
def get_backend():
    os.chdir( Config.get('Paths', 'Tools'))
    result = []
    arr = os.listdir(Config.get('Paths', 'Backends'))
    arr.sort()
    for element in arr:
        if element.find(".py") == -1 or element.find("discovery.py") != -1 or element.find("tools.py") != -1 or element.find("data.py") != -1 or element.find("base.py") != -1:
            continue
        else:
            result.append(element.replace('.py', ' '))
    return jsonify(result)

@app.route("/configs")
def get_configs():
    result = ["elk-defaultindex",
     "elk-defaultindex-filebeat",
     "elk-defaultindex-logstash",
                     "elk-linux",
                   "elk-windows",
                "elk-winlogbeat",
             "elk-winlogbeat-sp",
                    "powershell",
                "splunk-windows",
          "splunk-windows-index",
                   "splunk-zeek",
                        "sysmon",
                 "windows-audit",
              "windows-services"]
    return jsonify(result)

@app.route("/", methods=['POST'])
def convert():
    data = request.get_json()
    rule = str(base64.b64decode(request.json['rule']), "utf-8")

    os.chdir( Config.get('Paths', 'Tools'))

    f = open("./rule.yaml", "w")
    f.write(rule)
    f.close()

    sigmac = "python3 sigmac -t {} -c {} ./rule.yaml".format(data['target'], data['config']) #python3 sigmac -t splunk -c splunk-windows ../rules/windows/driver_load/driver_load_mal_creddumper.yml
    return subprocess.getoutput(sigmac)

@app.route("/hello")
def hello():
    os.chdir(Config.get('Paths', 'Tools'))
    return os. getcwd() 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)                            