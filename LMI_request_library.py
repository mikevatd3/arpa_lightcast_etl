import json
import requests

from reference import DETROIT_ZIPS
from framewrapper import convert_to_df, today


def software_development(auth):
    headers = {
        "Authorization": f"Bearer {auth['access_token']}",
        "Content-Type": "application/json"
    }

    url = "https://agnitio.emsicloud.com/emsi.us.industry/2024.2"

    payload = {

        "metrics": [
            {
                "name": "Jobs.2012",
                "as": "2012 Jobs",
            }, 
            {
                "name": "Earnings.2012",
                "as": "2012 Earnings",
            }, 
            {
                "name": "Jobs.2017",
                "as": "2017 Jobs",
            }, 
            {
                "name": "Earnings.2017",
                "as": "2017 Earnings",
            }, 
            {
                "name": "Jobs.2023",
                "as": "2023 Jobs",
            }, 
            {
                "name": "Earnings.2023",
                "as": "2023 Earnings",
            }, 
        ],

        "constraints": [
            {
                "dimensionName": "Area",
                "map": {
                    "Wayne County, MI": ["26163"],
                    "Oakland County, MI": ["26125"],
                    "Macomb County, MI": ["26099"],
                    "Michigan": ["26"],
                    # "Detroit City, Wayne County, MI": ["2616322000"], # This doesn't work
                    **DETROIT_ZIPS
                }
            },
            { 
                "dimensionName": "Industry", 
                "map": { 
                    "Software development": ["541511"],
                },
            } 
        ]
    }

    response = requests.request("post", url, headers=headers, json=payload)

    return convert_to_df(response.json())




def all_jobs(auth):
    headers = {
        "Authorization": f"Bearer {auth['access_token']}",
        "Content-Type": "application/json"
    }

    url = "https://agnitio.emsicloud.com/emsi.us.industry/2024.2"

    payload = {

        "metrics": [
            {
                "name": "Jobs.2012",
                "as": "2012 Jobs",
            }, 
            {
                "name": "Earnings.2012",
                "as": "2012 Earnings",
            }, 
            {
                "name": "Jobs.2017",
                "as": "2017 Jobs",
            }, 
            {
                "name": "Earnings.2017",
                "as": "2017 Earnings",
            }, 
            {
                "name": "Jobs.2023",
                "as": "2023 Jobs",
            }, 
            {
                "name": "Earnings.2023",
                "as": "2023 Earnings",
            }, 
        ],

        "constraints": [
            {
                "dimensionName": "Area",
                "map": {
                    "Wayne County, MI": ["26163"],
                    "Michigan": ["26"],
                    # "Detroit City, Wayne County, MI": ["2616322000"], # This doesn't work
                    **DETROIT_ZIPS
                }
            },
        ]
    }

    response = requests.request("post", url, headers=headers, json=payload)

    return convert_to_df(response.json())
