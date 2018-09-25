# importing the requests library 
import requests
import json

# https://jsonplaceholder.typicode.com/posts?id=2
# api-endpoint 
URL_GET = "https://jsonplaceholder.typicode.com/posts"
URL_POST = "http://httpbin.org/post"

# location given here 
key1="1"
key2='2'
# defining a params dict for the parameters to be sent to the API
PARAMS_GET = {'id':key1}
payload = {'key1': 'value1', 'key2': 'value2'}

# sending get request and saving the response as response object 
r = requests.get(url = URL_GET, params = PARAMS_GET)
r2 = requests.post(url = URL_POST, data = payload)

# extracting data in json format
try :
    data = r.json()
    data2 = r2.json()
    print (data)
    print ('======')
    print (data2)
except:
    print ('Error!')
