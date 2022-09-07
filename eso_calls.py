import requests
import json


BASE_URL = 'https://data.nationalgrideso.com/api/3/action/'


def get_json(url):

    response = requests.get(url)
    r_json = response.json()

    return r_json


def create_url(endpoint, url_params):

    url = f"{BASE_URL}{endpoint}?"

    for p in url_params:
        if type(url_params[p]) == str:
            url += f"&{p}={(url_params[p])}"
        else:
            url += f"&{p}={json.dumps(url_params[p])}"

    return url


def get_datastore_search(url_params):

    url = create_url('datastore_search', url_params)
    results = get_json(url)['result']['records']

    return results

