# -*- coding: utf-8 -*-

import subprocess
from flask_script import Manager
from app import create_app
from flask import request
import time


app = create_app()
manager = Manager(app)


def f_calc(num):
    sum = 1
    for i in range(1, num + 1):
        sum = sum * i
    return sum


@app.route("/start")
def calc_start():
    data = request.args
    return "result: %s" % f_calc(int(data.get('value', 30000)))


@app.route("/long")
def long_task():
    subprocess.Popen(["python", "/tmp/download.py"])
    return "OK"


if __name__ == "__main__":
    manager.run()
