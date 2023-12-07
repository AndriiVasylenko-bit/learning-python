import json

with open('api.json', 'r') as file:
    lines = file.readlines()

data = ''
for line in lines:
    data += line.strip()

js = json.loads(data)

# Keep this file separate

# https://apps.twitter.com/
# Create new App and get the four strings
def oauth():
    return {"consumer_key": js["consumer_keys"]["access_token"],
            "consumer_secret": js["consumer_keys"]["access_token_secret"],
            "token_key": js["authentication_tokens"]["access_token"],
            "token_secret": js["authentication_tokens"]["access_token_secret"]}