from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC3139428030d177192b3689e142b1c037'
auth_token = '4ae7f5d68e7e0a7116d417412c9c37a5'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='BABAN',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+16474606524'
                          )

print(message.sid)