from requests import Session

import config

class Conn():
    API_KEY = config.NASA_API_KEY
    BASE_URL = config.NASA_NEO_URL

    session = requests.Session()
    session.
