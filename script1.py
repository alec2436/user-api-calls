import numpy as np
import pandas as pd
import requests
import json


csvfilename = 'alec_user_permissions.csv'

A = np.array([1,2,3])

apikey_value = '237O5W4A60Z15BK0D50C8H553C4S59E29XT7CBJ6XZMMAN6736C5W9J3KOM8UK7C'
url1 = 'https://api.cloudcheckr.com/api/best_practice.json/get_best_practices?access_key=237O5W4A60Z15BK0D50C8H553C4S59E29XT7CBJ6XZMMAN6736C5W9J3KOM8UK7C&use_account=Alec%20Rajeev%27s%20Account'
url2 = 'https://api.cloudcheckr.com/api/account.json/grant_account?access_key=237O5W4A60Z15BK0D50C8H553C4S59E29XT7CBJ6XZMMAN6736C5W9J3KOM8UK7C&email=cloudcheckr1@protonmail.com&use_account=AWS-2150Account&all_access=1'
account_name1 = 'Alec%20Rajeev%27s%20Account'
account_name1 = 'AWS-2150Account'
email1 = 'cloudcheckr1@protonmail.com'

qa_api = "3DQ62BV6UIR889OK14Z05313A27Y82S3O4QHX3SXMDQJ3OP9G8T4BBF4F03N1JSY"
# resp = requests.get(url1)

print "hello pearson"

print A

df = pd.read_csv(csvfilename, sep=',', header=None)

B_numpy = df.values

# print B_numpy

for i in np.arange(0,10):
	# print B_numpy[i]
	print "\n"

print np.shape(B_numpy)[0]

def run_api(api_key,account_name):
	resp = requests.get('https://api.cloudcheckr.com/api/best_practice.json/get_best_practices?access_key=' + api_key + '&use_account=' + account_name)
	# print "running api"
	print resp.json()

def change_user_permissions_api(api_key,user_email,account_name):
	complete_url = 'https://api.cloudcheckr.com/api/account.json/grant_account?access_key=' + api_key + '&email=' + user_email + '&use_account=' + account_name + '&all_access=1'
	# print complete_url
	half_url = 'https://api.cloudcheckr.com/api/account.json/grant_account'

	data2 = {"email": user_email, "use_account": account_name, "all_access": "1"}

	resp = requests.post(half_url, data=json.dumps(data2), headers = {"Content-type": "application/json", "access_key": api_key})
	# resp = requests.get(complete_url)
	# qa_url = "https://qa.cloudcheckr.com/api/account.json/edit_user"
	# resp = requests.post(qa_url, data={"email": "dummy@cloudcheckr.com","role": "BasicUser"}, headers = {"access_key": "3DQ62BV6UIR889OK14Z05313A27Y82S3O4QHX3SXMDQJ3OP9G8T4BBF4F03N1JSY", "content-type": "application/json"})

	print "running api"
	print resp.json()


# run_api(apikey_value,account_name1)

change_user_permissions_api(apikey_value, email1, account_name1)