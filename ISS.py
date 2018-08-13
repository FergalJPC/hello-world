import json
import requests

url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)
result = json.loads(response.content.decode("utf-8"))

people = result['people']

number = result['number']

print('There are %s people in space:' %(number))
for i in people:
	print(i['name']+' in the %s' % i['craft'])
