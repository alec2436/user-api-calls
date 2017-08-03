import numpy as np
import pandas as pd
import json
import requests


csvfilename = 'alec_user_permissions2.csv'
apikey_value = '237O5W4A60Z15BK0D50C8H553C4S59E29XT7CBJ6XZMMAN6736C5W9J3KOM8UK7C'

df = pd.read_csv(csvfilename, sep=',', header=None)

B_numpy = df.values

# print B_numpy


def build_json_parameters(user_email,account_name,permissions_array):
	data2 = {
		"email": user_email,
		"use_account": account_name,
		"access": permissions_array[0],
		"savings": permissions_array[1],
		"best_practices": permissions_array[2],
		"alert": permissions_array[3],
		"cost_report": permissions_array[4],
		"resource_utilization_reports": permissions_array[5],
		"inventory": permissions_array[6],
		"security": permissions_array[7],
		"automation": permissions_array[8],
		"edit_emails": permissions_array[9],
		"blended_cost": permissions_array[10],
		"unblended_cost": permissions_array[11],
		"list_cost": permissions_array[12],
		"trending_reports": permissions_array[13],
		"change_monitoring": permissions_array[14],
		"account_notification": permissions_array[15],
		"see_partner_tool": 0,
		"edit_partner_tool": 0,
		"see_api_keys": permissions_array[18]





	}
	return json.dumps(data2)



def change_user_permissions_api(api_key,user_email,account_name):
	half_url = 'https://api.cloudcheckr.com/api/account.json/grant_account'

	api_parameters = {"email": user_email, "use_account": account_name, "all_access": "1"}

	resp = requests.post(half_url, data=json.dumps(api_parameters), headers = {"Content-type": "application/json", "access_key": api_key})
	print "running api for account: " + account_name
	print "running api for user: " + user_email
	print resp.json()

def change_user_permissions_api2(api_key,json_dump2):
	half_url = 'https://api.cloudcheckr.com/api/account.json/grant_account'

	resp = requests.post(half_url, data=json_dump2, headers = {"Content-type": "application/json", "access_key": api_key})
	# print "running api for account: " + account_name
	# print "running api for user: " + user_email
	print resp.json()


for i in np.arange(1, np.shape(B_numpy)[0]):
	print B_numpy[i][0]
	if int(B_numpy[i][6]): # if the account has Access as true
		input_paramters = build_json_parameters(B_numpy[i][0],B_numpy[i][5],B_numpy[i][6:25])
		change_user_permissions_api2(apikey_value, input_paramters)
