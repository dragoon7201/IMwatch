from twilio.rest import Client

my_num = '+12028001446'

account = 'AC4ba9f6803810af776c0c3247f0810b6d'

token = 'ee24a939931fd532bc1889ec0c8f0066'

client = Client(account, token)

call = client.calls.create(

    to='+13068808818',
    from_=my_num)

message = client.messages.create(
    to='+13068808818',
    from_=my_num,
    body='twilio test msg')

print(call.sid)
