import requests
from tornado.escape import json_decode, json_encode
import json

#url = "http://38.143.19.31:8080/v1/worker/ss/add-job"
url = "http://154.13.29.149:10000/v1/worker/ss/add-job"

config = {"port":42116,"passwd":"2p41PwK8","method":"salsa20","mode":"tcp_and_udp","timeout":300}
data_json = json.dumps(config)

print('-----------------')

#para_file = "add.json"
#with open(para_file) as f:
#    config = json.load(f)
#    data_json = json_encode(config)
#    print(type(config), config)
#

rj = requests.post(url, data_json)
print(rj)
print(rj.text)
print(rj.content)
