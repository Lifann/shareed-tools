import json
from tornado.escape import json_decode, json_encode


content = '{"a":1, "b":"rua", "c": true}'

print(content)
js = json_decode(content)
print(type(js), js)

for x in js:
	print(x, js[x])
