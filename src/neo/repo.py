import json

from neo import Neo
import repo


def get_feed():
    response = repo.get_feed()

    print(response)

    # raw_data = json.loads(response)
    #
    # feed = [parse(result) for result in raw_data]
    #
    # return feed


def parse(result):
    Neo.from_dict(result)
