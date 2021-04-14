import requests
from tornado.escape import json_decode, json_encode
import json

url = "http://38.143.19.31:8080/v1/worker/stop-job"

data_json = json.dumps({
    "test": "rua",
})

para_file = "kandian_video_config.json"
with open(para_file) as f:
    config = json.load(f)
    data_json = json_encode(config)
    #print(type(config), config)

#print(type(json.dumps(config)), "\n", json.dumps(config))
#print(type(res), "\n", res)

rj = requests.post(url, data_json)
print(rj)
print(rj.text)
print(rj.content)
