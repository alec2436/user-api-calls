import numpy as np
import pandas as pd
import requests
import json


csvfilename = 'alec_user_permissions.csv'

apikey_value = '237O5W4A60Z15BK0D50C8H553C4S59E29XT7CBJ6XZMMAN6736C5W9J3KOM8UK7C'
account_name1 = 'Alec Rajeev\'s Account'
email1 = 'cloudcheckr2@protonmail.com'


def run_get_api(api_key,account_name):
	complete_url = 'https://api.cloudcheckr.com/api/account.json/grant_account?access_key=' + api_key + '&email=' + user_email + '&use_account=' + account_name + '&all_access=1'
	resp = requests.get(complete_url)
	print "running api"
	print resp.json()

def change_user_permissions_api(api_key,user_email,account_name):
	half_url = 'https://api.cloudcheckr.com/api/account.json/grant_account'

	api_parameters = {"email": user_email, "use_account": account_name, "all_access": "1"}

	resp = requests.post(half_url, data=json.dumps(api_parameters), headers = {"Content-type": "application/json", "access_key": api_key})
	print "running api for account: " + account_name
	print "running api for user: " + user_email
	print resp.json()

change_user_permissions_api(apikey_value, email1, account_name1)