#Building trading bot. 

from neo_api_client import NeoAPI


def on_message(message):
    print(message)
    
def on_error(error_message):
    print(error_message)

def on_close(message):
    print(message)
    
def on_open(message):
    print(message)

client = NeoAPI(consumer_key="mUvINsjJpDv_oSxpYdnrkQ9oFDUa", consumer_secret="gbghdPa4nHLXgSUafMpmloXhXvMa", environment='prod',
                access_token=None, neo_fin_key=None)

x = "+91XXXXXXXXXX"
y = "XXXXXX"

print(client.login(mobilenumber=x, password=y))

#client.session_2fa(OTP="XXXX")

# client.on_message = on_message  # called when message is received from websocket
# client.on_error = on_error  # called when any error or exception occurs in code or websocket
# client.on_close = on_close  # called when websocket connection is closed
# client.on_open = on_open
#
# print(client.scrip_master())

