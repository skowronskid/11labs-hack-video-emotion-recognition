import requests
from requests.auth import HTTPBasicAuth

password = "bb96ac75f83b566bdf6fe03dffec5293"


def get_keys():
    url = "https://11labs-hackathon-tokens.vercel.app/api/tokens"
    username = "sheeesh"
    return requests.get(url, auth=HTTPBasicAuth(username, password)).json() 



