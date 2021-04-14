import json
import requests
from tornado.escape import json_decode, json_encode
import os, sys, time
import traceback

path = './context/'
filenames = os.listdir(path)
ip_addr = []
for i, v in enumerate(filenames):
    ip = v.replace('.txt', '')
    ip_addr.append(ip)
    filenames[i] = path + v

#print(filenames)
print(ip_addr)

for idx, a_file in enumerate(filenames):
    with open(a_file) as f:
        for line in f:
            if line==None: continue
            line = line.replace('\n', '')
            #print('type: {} \t\t line: {}'.format(type(line), line))
            str_json = json_decode(line)
            data_json = json_encode(str_json)
            #print(js)

            url = "http://{}:8080/v1/worker/ss/add-job".format(ip_addr[idx])
            #print(type(data_json), data_json)
            #print(url)
            try:
                rj = requests.post(url, data_json)
                print('----------------')
                print('req: {}'.format(line))
                print(url)
                print(rj, rj.text, rj.content)
            except:
                print(traceback.format_exc())
