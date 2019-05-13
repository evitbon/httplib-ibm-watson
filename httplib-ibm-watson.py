import httplib
import urllib
import base64
import json
 
host = "gateway.watsonplatform.net"
#url = "/visual-recognition/api/v3/detect_faces?version=2018-03-19"
url = "/visual-recognition/api/v3/detect_faces?"
username = 'apikey'
password = '<your-api-key>'
version = '2018-03-19'
image = "<your-image:jpg,png>"

# read the binary data of the picture
data = open(image, 'rb')
params = url + urllib.urlencode({'version': version})
auth = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
headers = { "Authorization": "Basic %s" % auth }
conn = httplib.HTTPSConnection( host , 443)
conn.request( "POST", params, data, headers)
response = conn.getresponse()
# returns "True" or "False" if failed
results = response.read()
#print response.read()
print "Results:\n", results
with open("result.json", "w") as file:
	json.dump(results, file, indent=2, ensure_ascii=False)
# status for debugging
#print response.status, response.reason
# close connection
conn.close()
# close files
data.close()
