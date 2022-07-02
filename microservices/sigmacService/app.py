import base64
from flask import Flask, request
import subprocess
import os
import subprocess
import configparser


app = Flask(__name__)
Config = configparser.ConfigParser()
configFilePath = './config.ini'
Config.read(configFilePath)

@app.route("/lists")
def get_list():
    target = '--lists'
    sigmac = "sigmac {}".format(target)
    return subprocess.getoutput(sigmac) #sigmac --lists

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

                                                