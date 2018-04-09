# -*- coding: utf-8 -*-

import thread
import time
import requests
 

def send_requests(thread_name):

    for i in range(10000):
        url = "http://ess-dev.1tai.com/start"

        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "036d6ef8-13f4-5c72-bda7-bf74a6e7c6be"
        }
        response = requests.request("GET", url, headers=headers)
        print thread_name, response.text[:16]



thread.start_new_thread( send_requests, ("Thread-1", ))
thread.start_new_thread( send_requests, ("Thread-2", ))
thread.start_new_thread( send_requests, ("Thread-3", ))
thread.start_new_thread( send_requests, ("Thread-4", ))
thread.start_new_thread( send_requests, ("Thread-5", ))
thread.start_new_thread( send_requests, ("Thread-6", ))

thread.start_new_thread( send_requests, ("Thread-7", ))
thread.start_new_thread( send_requests, ("Thread-8", ))
thread.start_new_thread( send_requests, ("Thread-9", ))
thread.start_new_thread( send_requests, ("Thread-10", ))
thread.start_new_thread( send_requests, ("Thread-11", ))
thread.start_new_thread( send_requests, ("Thread-12", ))

thread.start_new_thread( send_requests, ("Thread-7", ))
thread.start_new_thread( send_requests, ("Thread-8", ))
thread.start_new_thread( send_requests, ("Thread-9", ))
thread.start_new_thread( send_requests, ("Thread-10", ))
thread.start_new_thread( send_requests, ("Thread-11", ))
thread.start_new_thread( send_requests, ("Thread-12", ))
thread.start_new_thread( send_requests, ("Thread-1", ))
thread.start_new_thread( send_requests, ("Thread-2", ))
thread.start_new_thread( send_requests, ("Thread-3", ))
thread.start_new_thread( send_requests, ("Thread-4", ))
thread.start_new_thread( send_requests, ("Thread-5", ))
thread.start_new_thread( send_requests, ("Thread-6", ))

thread.start_new_thread( send_requests, ("Thread-7", ))
thread.start_new_thread( send_requests, ("Thread-8", ))
thread.start_new_thread( send_requests, ("Thread-9", ))
thread.start_new_thread( send_requests, ("Thread-10", ))
thread.start_new_thread( send_requests, ("Thread-11", ))
thread.start_new_thread( send_requests, ("Thread-12", ))

thread.start_new_thread( send_requests, ("Thread-7", ))
thread.start_new_thread( send_requests, ("Thread-8", ))
thread.start_new_thread( send_requests, ("Thread-9", ))
thread.start_new_thread( send_requests, ("Thread-10", ))
thread.start_new_thread( send_requests, ("Thread-11", ))
thread.start_new_thread( send_requests, ("Thread-12", ))
thread.start_new_thread( send_requests, ("Thread-1", ))
thread.start_new_thread( send_requests, ("Thread-2", ))
thread.start_new_thread( send_requests, ("Thread-3", ))
thread.start_new_thread( send_requests, ("Thread-4", ))
thread.start_new_thread( send_requests, ("Thread-5", ))
thread.start_new_thread( send_requests, ("Thread-6", ))

thread.start_new_thread( send_requests, ("Thread-7", ))
thread.start_new_thread( send_requests, ("Thread-8", ))
thread.start_new_thread( send_requests, ("Thread-9", ))
thread.start_new_thread( send_requests, ("Thread-10", ))
thread.start_new_thread( send_requests, ("Thread-11", ))
thread.start_new_thread( send_requests, ("Thread-12", ))

thread.start_new_thread( send_requests, ("Thread-7", ))
thread.start_new_thread( send_requests, ("Thread-8", ))
thread.start_new_thread( send_requests, ("Thread-9", ))
thread.start_new_thread( send_requests, ("Thread-10", ))
thread.start_new_thread( send_requests, ("Thread-11", ))
thread.start_new_thread( send_requests, ("Thread-12", ))
thread.start_new_thread( send_requests, ("Thread-1", ))
thread.start_new_thread( send_requests, ("Thread-2", ))
thread.start_new_thread( send_requests, ("Thread-3", ))
thread.start_new_thread( send_requests, ("Thread-4", ))
thread.start_new_thread( send_requests, ("Thread-5", ))
thread.start_new_thread( send_requests, ("Thread-6", ))

thread.start_new_thread( send_requests, ("Thread-7", ))
thread.start_new_thread( send_requests, ("Thread-8", ))
thread.start_new_thread( send_requests, ("Thread-9", ))
thread.start_new_thread( send_requests, ("Thread-10", ))
thread.start_new_thread( send_requests, ("Thread-11", ))
thread.start_new_thread( send_requests, ("Thread-12", ))

thread.start_new_thread( send_requests, ("Thread-7", ))
thread.start_new_thread( send_requests, ("Thread-8", ))
thread.start_new_thread( send_requests, ("Thread-9", ))
thread.start_new_thread( send_requests, ("Thread-10", ))
thread.start_new_thread( send_requests, ("Thread-11", ))
thread.start_new_thread( send_requests, ("Thread-12", ))
thread.start_new_thread( send_requests, ("Thread-1", ))
thread.start_new_thread( send_requests, ("Thread-2", ))
thread.start_new_thread( send_requests, ("Thread-3", ))
thread.start_new_thread( send_requests, ("Thread-4", ))
thread.start_new_thread( send_requests, ("Thread-5", ))
thread.start_new_thread( send_requests, ("Thread-6", ))

thread.start_new_thread( send_requests, ("Thread-7", ))
thread.start_new_thread( send_requests, ("Thread-8", ))
thread.start_new_thread( send_requests, ("Thread-9", ))
thread.start_new_thread( send_requests, ("Thread-10", ))
thread.start_new_thread( send_requests, ("Thread-11", ))
thread.start_new_thread( send_requests, ("Thread-12", ))

thread.start_new_thread( send_requests, ("Thread-7", ))
thread.start_new_thread( send_requests, ("Thread-8", ))
thread.start_new_thread( send_requests, ("Thread-9", ))
thread.start_new_thread( send_requests, ("Thread-10", ))
thread.start_new_thread( send_requests, ("Thread-11", ))
thread.start_new_thread( send_requests, ("Thread-12", ))
thread.start_new_thread( send_requests, ("Thread-1", ))
thread.start_new_thread( send_requests, ("Thread-2", ))
thread.start_new_thread( send_requests, ("Thread-3", ))
thread.start_new_thread( send_requests, ("Thread-4", ))
thread.start_new_thread( send_requests, ("Thread-5", ))
thread.start_new_thread( send_requests, ("Thread-6", ))

thread.start_new_thread( send_requests, ("Thread-7", ))
thread.start_new_thread( send_requests, ("Thread-8", ))
thread.start_new_thread( send_requests, ("Thread-9", ))
thread.start_new_thread( send_requests, ("Thread-10", ))
thread.start_new_thread( send_requests, ("Thread-11", ))
thread.start_new_thread( send_requests, ("Thread-12", ))

thread.start_new_thread( send_requests, ("Thread-7", ))
thread.start_new_thread( send_requests, ("Thread-8", ))
thread.start_new_thread( send_requests, ("Thread-9", ))
thread.start_new_thread( send_requests, ("Thread-10", ))
thread.start_new_thread( send_requests, ("Thread-11", ))
thread.start_new_thread( send_requests, ("Thread-12", ))
thread.start_new_thread( send_requests, ("Thread-1", ))
thread.start_new_thread( send_requests, ("Thread-2", ))
thread.start_new_thread( send_requests, ("Thread-3", ))
thread.start_new_thread( send_requests, ("Thread-4", ))
thread.start_new_thread( send_requests, ("Thread-5", ))
thread.start_new_thread( send_requests, ("Thread-6", ))

thread.start_new_thread( send_requests, ("Thread-7", ))
thread.start_new_thread( send_requests, ("Thread-8", ))
thread.start_new_thread( send_requests, ("Thread-9", ))
thread.start_new_thread( send_requests, ("Thread-10", ))
thread.start_new_thread( send_requests, ("Thread-11", ))
thread.start_new_thread( send_requests, ("Thread-12", ))

thread.start_new_thread( send_requests, ("Thread-7", ))
thread.start_new_thread( send_requests, ("Thread-8", ))
thread.start_new_thread( send_requests, ("Thread-9", ))
thread.start_new_thread( send_requests, ("Thread-10", ))
thread.start_new_thread( send_requests, ("Thread-11", ))
thread.start_new_thread( send_requests, ("Thread-12", ))
thread.start_new_thread( send_requests, ("Thread-1", ))
thread.start_new_thread( send_requests, ("Thread-2", ))
thread.start_new_thread( send_requests, ("Thread-3", ))
thread.start_new_thread( send_requests, ("Thread-4", ))
thread.start_new_thread( send_requests, ("Thread-5", ))
thread.start_new_thread( send_requests, ("Thread-6", ))

thread.start_new_thread( send_requests, ("Thread-7", ))
thread.start_new_thread( send_requests, ("Thread-8", ))
thread.start_new_thread( send_requests, ("Thread-9", ))
thread.start_new_thread( send_requests, ("Thread-10", ))
thread.start_new_thread( send_requests, ("Thread-11", ))
thread.start_new_thread( send_requests, ("Thread-12", ))

thread.start_new_thread( send_requests, ("Thread-7", ))
thread.start_new_thread( send_requests, ("Thread-8", ))
thread.start_new_thread( send_requests, ("Thread-9", ))
thread.start_new_thread( send_requests, ("Thread-10", ))
thread.start_new_thread( send_requests, ("Thread-11", ))
thread.start_new_thread( send_requests, ("Thread-12", ))
thread.start_new_thread( send_requests, ("Thread-1", ))
thread.start_new_thread( send_requests, ("Thread-2", ))
thread.start_new_thread( send_requests, ("Thread-3", ))
thread.start_new_thread( send_requests, ("Thread-4", ))
thread.start_new_thread( send_requests, ("Thread-5", ))
thread.start_new_thread( send_requests, ("Thread-6", ))

thread.start_new_thread( send_requests, ("Thread-7", ))
thread.start_new_thread( send_requests, ("Thread-8", ))
thread.start_new_thread( send_requests, ("Thread-9", ))
thread.start_new_thread( send_requests, ("Thread-10", ))
thread.start_new_thread( send_requests, ("Thread-11", ))
thread.start_new_thread( send_requests, ("Thread-12", ))

thread.start_new_thread( send_requests, ("Thread-7", ))
thread.start_new_thread( send_requests, ("Thread-8", ))
thread.start_new_thread( send_requests, ("Thread-9", ))
thread.start_new_thread( send_requests, ("Thread-10", ))
thread.start_new_thread( send_requests, ("Thread-11", ))
thread.start_new_thread( send_requests, ("Thread-12", ))

while True:
    time.sleep(1)