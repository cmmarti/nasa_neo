class Neo():
    def __init__(self, _id, name, potentially_hazardous, close_approach_date):
        self._id = _id
        self.name = name
        self.potentially_hazardous = potentially_hazardous
        self.close_approach_date = close_approach_date

    @classmethod
    def from_dict(cls, dict_neo):
        # TODO: move this to client
        return Neo(dict_neo['id'],
                   dict_neo['name'],
                   dict_neo['is_potentially_hazardous_asteroid'],
                   dict_neo['close_approach_data'][0]['close_approach_date']
                   )
