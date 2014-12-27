from redis import Redis

INITIAL_VALUE = 0


class Auid(object):
    def __init__(self, name, client=Redis()):
        self.name = name
        self.client = client

    def incr(self):
        value = self.client.incr(self.name)
        return int(value)

    def get(self):
        value = self.client.get(self.name)
        return int(value) if value else INITIAL_VALUE
