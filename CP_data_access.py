from pathlib import Path
import json
import requests

from auth_helper import retrieve_auth, auto_refresh
from framewrapper import today



@auto_refresh
def main():
    auth = retrieve_auth()
    headers = {
        "Authorization": f"Bearer {auth['access_token']}",
        "Content-Type": "application/json"
    }

    url = "https://emsiservices.com/career-pathways/dimensions/lotspecocc/feederjobs"

    payload = {
        "id": "23141014",
        "categories": ["Advancement", "LateralAdvancement", "Similar", "LateralTransition"],
        "region": {"nation": "us"},
        "limit": 3
    }

    response = requests.post(url, json=payload, headers=headers)

    with open(Path.cwd() / "CP_results" / f"dims_{today()}.json", "w") as f:
        json.dump(response.json(), f, indent=4)


if __name__ == "__main__":
    main()