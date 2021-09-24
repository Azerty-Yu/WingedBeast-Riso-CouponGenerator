# Download the helper library from https://www.twilio.com/docs/python/install
import os
import json
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure

with open('../cred.json') as file:
	cred = json.load(file)
	account_sid =  cred['account_sid']
	auth_token = cred['auth_token']
	outgoing_number = cred['outgoing_number']
	user_number = cred['user_number']


client = Client(account_sid, auth_token)
message = client.messages \
                .create(
                     body="test",
                     from_=outgoing_number,
                     to=user_number
                 )

print(message.sid)
