import json
import requests


"""
This module handles updating the auth token automatically as it times out,
and makes it easier to read in the saved token from the data access function.
"""


def refresh_auth():
    with open("config.json") as f:
        config = json.load(f)

        CLIENT_ID = config["username"]
        CLIENT_SECRET =  config["secret"]

    url = "https://auth.emsicloud.com/connect/token"

    payload = f"client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&grant_type=client_credentials&scope=career-pathways"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.request("POST", url, data=payload, headers=headers)

    with open("auth.json", "w") as f:
        json.dump(response.json(), f)


def retrieve_auth():
    with open("auth.json") as f:
        return json.load(f)


def auto_refresh(main):
    # Right now 'main' reads the auth within the function 

    def inner():
        try:
            main()

        except:
            refresh_auth()
            main()
    
    return inner

