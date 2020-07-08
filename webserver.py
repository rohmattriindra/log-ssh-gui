#!/usr/bin/python3
from flask import Flask, render_template, request
from pprint import pprint
import subprocess
import os 

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/ssh_log", methods=["GET"])
def ssh():
    return render_template("ssh_log.html")

@app.route("/ssh_log/send", methods=["POST"])
def ssh_execute():
    cmd = "python3", "ssh.py"
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    result,err = p.communicate()
    return render_template("log_result.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")