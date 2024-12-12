import json
import requests
from auth_helper import retrieve_auth, auto_refresh


@auto_refresh
def main():
    auth = retrieve_auth()
    headers = {
        "Authorization": f"Bearer {auth['access_token']}",
        "Content-Type": "application/json"
    }

    url = "https://agnitio.emsicloud.com/meta/dataset/EMSI.us.Occ.Hires.Seps/2024.2"

    response = requests.request("get", url, headers=headers)

    with open("metadata.json", "w") as f:
        json.dump(response.json(), f, indent=4)



if __name__ == "__main__":
    main()