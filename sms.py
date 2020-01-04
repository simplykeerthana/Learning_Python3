# send sms using python script
#twilio api for communications, also have to sign up for services

from twilio.rest import client

account_sid = 'the key'
auth_token = '[authttoken]'
client = client(account_sid, auth_token)

message = client.message.create(from = 'twilio phonenumber', body='cant believe this works'.to='reciever phonenumber')

print(message)
 