#!/usr/bin/env python3
import requests
import json

site = 'https://interns.bcgdvsydney.com'
apiKeyEndpoint = '/api/v1/key'

response = requests.get(site + apiKeyEndpoint)
print(response.status_code)
json_data = json.loads(response.text)
print('Key: ' + json_data['key'])
print('Expires: ' + json_data['expires'])

file = open('key.txt', 'w')
file.write(json_data['key'] + '\n' + json_data['expires'])

payload = {
    'name': 'Andy Yu',
    'email': 'andy.yu2k@gmail.com'
}

subEndpoint = '/api/v1/submit?apiKey='
submission = requests.post(site + subEndpoint + json_data['key'], json = payload)

print(submission.status_code)






