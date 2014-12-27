from auid import Auid
from redis import StrictRedis


def store_tracks(redis_tracks):
    '''
    # Parameters:
    * redis_tracks: [(artist1, title1), (artist2, title2)]

    Three steps
        set track:1:artist: Arcade Fire
        set track:1:title: wake up
        set track:Arcade fire wake up:id: 1
    '''
    client = StrictRedis()
    uid = Auid("Track")
    for track in redis_tracks:
        track_id = uid.incr()
        artist = track[0]
        title = track[1]
        keyname_for_artist = "track:%s:artist" % (track_id)
        keyname_for_title = "track:%s:title" % (track_id)
        keyname_for_total = "track:%s %s:id" % (artist, title)
        client.set(keyname_for_artist, artist)
        client.set(keyname_for_title, title)
        client.set(keyname_for_total, track_id)


def init_track(track):
    '''
    # Parameters:
    * track : (artist, title)
    '''
    info = track[0] + track[1]
    client = StrictRedis()
    client.sadd("uncrawled", info)


def is_in_uncrawled(track):
    '''
    # Parameters:
    * track : (artist, title)
    '''
    pass


class Credis(object):
    def __init__(self):
        self.client = StrictRedis()

    def init_track(self, track):
        '''
        # Parameters:
        * track : (artist, title)
        '''
        info = track[0] + track[1]
        self.client.sadd("uncrawled", info)

    def is_in_uncrawled(self, track):
        info = unicode(track[0].artist) + unicode(track[0].title)
        return self.client.sismember('uncrawled', info)

    def remove_from_uncrawled(self, track):
        info = unicode(track[0].artist) + unicode(track[0].title)
        return self.client.srem("uncrawled", info)
