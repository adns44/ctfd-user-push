#!/usr/bin/python3

import requests
import json

# input file
infile = "ctfusers.txt"
# CTFd API token
ctfd_token=""
#CTFd URL
url="http://localhost"

# Variables in the nth position of the line. Username,email,password,bracket
#username=1
#email=2
#password=3
#bracket=4

def get_brackets(url, ctfd_token):
	brackets={}
	headers = {
		'Authorization': 'Token '+ctfd_token,
	}

	response = requests.get(''+url+'/api/v1/brackets', headers=headers)
	data=json.loads(response.text)
	items=list(data['data'])
	for item in items:
		if item['type'] == 'users':
			brackets[item['name']]=item['id']
	return brackets

def create_bracket(ctfd_token, bracket):
	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'Token '+ctfd_token,
	}
	data={'name': bracket, 'type': 'users', 'description': ''}
	resp = requests.post(''+url+'/api/v1/brackets', json=data, headers=headers)



brackets=get_brackets(ctfd_token)


with open(infile) as ff:
	for i in ff:
		username,email,password,bracket=i.strip().split(',')
		if bracket not in brackets:
			create_bracket(ctfd_token,bracket)
			brackets=get_brackets(ctfd_token)
		headers = {
			'Content-Type': 'application/json',
			'Authorization': 'Token '+ctfd_token,
		}
		data={"name": username, "email": email, "password": password, "bracket_id": brackets[bracket] }
		requests.post(''+url+'/api/v1/users', headers=headers, json=data)

