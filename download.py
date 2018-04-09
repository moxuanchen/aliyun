# -*- coding: utf-8 -*-

import time
import subprocess

for i in range(10000):
    ret = subprocess.Popen(["wget", "http://www.baidu.com"])
    ret.wait()
    time.sleep(1)