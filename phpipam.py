from requests.auth import HTTPBasicAuth
import requests

#################### Definition Index ######################
"""

phpipam_generate_token 							# returns phpipam_token
phpipam_headers 								# returns phpipam_headers
phpipam_get_requests 							# returns get response from xpath request


"""
######################## End Index #########################



def phpipam_generate_token(**kwargs):
	############### Start Functon Info ####################
	"""
	This function requests a new token from phpipam using the credentials provided

	ex return:
	'EPA5PW3LfUPvNO6AFP3LPHBS'

	args = {
		'phpipam_url': 'https://phpipam.acme.com',						# URL for ipam server
		'phpipam_app_id': 'devapi'										# API application id under api management
		'phpipam_username': 'admin',									# Username to create token for
		'phpipam_password': 'password'									# Password for user
		'ssl_verify': False 											# Verify SSL cert True or False
		}

	"""
	############### End Functon Info ####################
	################# Format XPATH ######################
	phpipam_xpath = '{0}{1}{2}{3}'.format(kwargs['phpipam_url'], "/api/", kwargs['phpipam_app_id'], "/user/")
	############ Begin Standard response ################
	if 'ssl_verify' in kwargs:
		response = requests.request("POST", phpipam_xpath, auth = HTTPBasicAuth(kwargs['phpipam_username'], kwargs['phpipam_password']), verify = kwargs['ssl_verify'])
	else:
		response = requests.request("POST", phpipam_xpath, auth = HTTPBasicAuth(kwargs['phpipam_username'], kwargs['phpipam_password']))
	if response.json()['code'] == 200 and response.json()['success'] == True:
	############## End Standard response ################	
		return(response.json()['data']['token'])
	else:
		print('phpipam_generate_token ', response.json()['code'])



def phpipam_headers(**kwargs):
	############### Start Functon Info ####################
	"""
	This function creates a formated headers

	ex return:
	{'phpipam-token': 'EPA5PW3LfUPvNO6AFP3LPHBS'}

	ex args:
	subnet_id = '7'										# The ID of subnet in phpipam
	kwargs = {
		'phpipam_url': 'https://phpipam.acme.com',		# URL for ipam server
		'app_id': 'devapi'								# API application id under api management
		'username': 'admin', 							# Use one token or Username / Password
		'password': 'password',							# Use one token or Username / Password
		'ssl_verify': False, 							# Verify SSL cert True or False (optional)
		'token': '1234567890'							# Use one token or Username / Password
		}

	"""
	############### End Functon Info ####################
	########## Create or use existing token #############
	try:
		if 'phpipam_username' in kwargs and 'phpipam_password' in kwargs:
			phpipam_generate_token_args = {
				'phpipam_url': kwargs['phpipam_url'], 
				'phpipam_username': kwargs['phpipam_username'], 
				'phpipam_password': kwargs['phpipam_password'],
				'phpipam_app_id': kwargs['phpipam_app_id']
				}
			phpipam_token = phpipam_generate_token(**phpipam_generate_token_args)
		else:
			phpipamn_token = kwargs['phpipam_token']
	except:
		print("Missing authentication parameter (phpipam_username, phpipam_password, or phpipam_token)")
	################ Format headers #####################
	phpipam_headers = {'phpipam-token': phpipam_token}
	return(phpipam_headers)




def phpipam_get_requests(phpipam_xpath, phpipam_headers, **kwargs):
	############### Start Functon Info ####################
	"""
	This function will check if an ssl_verify arg was sent on a get request and return the response if a 200 is recieved
    Otherwise it will print status code

	kwargs = {
		'phpipam_url': 'https://phpipam.acme.com',		# URL for ipam server
		'app_id': 'devapi'								# API application id under api management
		'username': 'admin',							# Use one token or Username / Password
		'password': 'password',							# Use one token or Username / Password
		'ssl_verify': False,							# Verify SSL cert True or False (optional)
		'token': '1234567890'							# Use one token or Username / Password
		}
	"""
	############### End Functon Info ####################
	############### Begin GET request ###################
	if 'ssl_verify' in kwargs:
		phpipam_get_response = requests.request("GET", phpipam_xpath, headers = phpipam_headers, verify = kwargs['ssl_verify'])
	else:
		phpipam_get_response = requests.request("GET", phpipam_xpath, headers = phpipam_headers)
	if phpipam_get_response.json()['code'] == 200 and phpipam_get_response.json()['success'] == True:
		return(phpipam_get_response)
	else:
		print('fn phpipam_get_requests retruned ', phpipam_xpath, phpipam_get_response.json())
	############## End Standard response ################	



