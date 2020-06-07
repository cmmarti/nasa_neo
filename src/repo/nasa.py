from urllib.parse import urljoin

import requests

from . import config


BASE_URL = config.NASA_NEO_URL


def get_feed():
    url = urljoin(BASE_URL, "feed/today")

    payload = {
      'api_key': config.NASA_API_KEY,
      'detailed': 'true'
    }

    response = requests.get(url, params=payload)

    return response.json()
