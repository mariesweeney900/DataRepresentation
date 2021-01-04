# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 14:52:14 2021

@author: pauls
"""
#https://www.nylas.com/blog/use-python-requests-module-rest-apis/


import requests

response = requests.get('https://google.com/')
print(response)



import requests
response = requests.get("http://api.open-notify.org/astros.json")
print(response)



query = {'lat':'45', 'lon':'180'}
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
print(response.json())


# Create a new resource
response = requests.post('https://httpbin.org/post', data = {'key':'value'})
# Update an existing resource
requests.put('https://httpbin.org/put', data = {'key':'value'})

#retrieve metadata
print(response.headers["date"]) 


requests.get(
  'https://api.github.com/user', 
  auth=HTTPBasicAuth('username', 'password')
 )


curl -G \
  --url 'https://api.nylas.com/oauth/authorize' \
  -H 'Authorization: Basic ENCODED_CLIENT_SECRET' \
  -d 'client_id=nylas_client_id' \
  -d 'redirect_uri=http://example.com/nylas_callback' \
  -d 'response_type=code' \
  -d 'scopes=email.read_only,calendar.read_only,contacts.read_only' \
  -d 'login_hint=my_email@example.com' \
  -d 'state=MyCustomStateString'
  



