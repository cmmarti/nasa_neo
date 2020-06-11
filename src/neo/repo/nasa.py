from urllib.parse import urljoin

import requests

import config
import session

API_KEY = config.NASA_API_KEY
BASE_URL = config.NASA_NEO_URL


def get_today_feed(detailed=True):
    url = urljoin(BASE_URL, "feed/today")
    payload = {
      'api_key': API_KEY

    }





def get_neo_sentry(active=True):
    session = requests.Session()

    url = urljoin(BASE_URL, "neo/sentry")
    payload = {
      'api_key': API_KEY,
      'is_active': is_active,
      'page': 0,
      'size': 100
    }

    first_page = session.get(url, params=payload).json()
    yield first_page
    num_pages = first_page['last_page']

    for page in range(2, num_pages + 1):
        next_page = session.get(url, params={'page': page}).json()
        yield next_page
