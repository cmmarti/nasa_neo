from datetime import datetime
from urllib.parse import urljoin


import requests

from . import config
from .neo import Neo


BASE_URL = config.NASA_NEO_URL


def get_feed():
    url = urljoin(BASE_URL, "feed/today")

    payload = {
      'api_key': config.NASA_API_KEY,
      'detailed': 'true'
    }

    response = requests.get(url, params=payload)

    return parse(response)


def parse(response):

    TODAY_DATE = datetime.today().strftime('%Y-%m-%d')

    raw_data = response.json()
    raw_objects = raw_data['near_earth_objects'][TODAY_DATE]

    result = [Neo.from_dict(raw_neo) for raw_neo in raw_objects]

    return result
