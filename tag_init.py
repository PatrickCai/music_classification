#! /usr/bin/env python
# -- encoding:utf - 8 --
import sys
import cPickle
import gevent

from gevent import monkey
monkey.patch_all()

from config import constants, database
from credis import credis
from credis.credis import Credis
reload(sys)
sys.setdefaultencoding('utf-8')

tracks = cPickle.load(open("top_tracks", "r"))

# tracks = tracks[81:82]

tag_value = []

all_tags = []  # each element [(artist, title), tags]


def get_tags(track):
    tags = track[1]
    for tag in tags:
        if str(tag[0]) in constants.VALID_TAGS:
            if int(tag[1]) < constants.MIDDLE_VALUE:
                value = 1
            elif int(tag[1]) >= constants.MIDDLE_VALUE:
                value = 2
            else:
                break
            artist = str(track[0][0])
            title = str(track[0][1])
            tag = str(tag[0])
            database.store_tag(artist, title, tag, value)


def init_all_tracks(client):
    '''Put all tracks info into redis
    '''
    tracks = cPickle.load(open("top_tracks", "r"))
    for track in tracks:
        artist = unicode(track[0].artist)
        title = unicode(track[0].title)
        client.init_track((artist, title))


def download_tags(track, client):
    tags = track[0].get_top_tags()
    tag = [(track[0].artist, track[0].title), tags]
    all_tags.append(tag)
    print(len(all_tags))
    cPickle.dump(all_tags, open('tags', 'a'))
    client.remove_from_uncrawled(track)
    if len(all_tags) >= 80:
        exit(0)


def is_in_uncrawled(track):
    return credis.is_in_uncrawled(track)


if __name__ == "__main__":
    client = Credis()
    # init_all_tracks(client)
    gevent_spawns = [gevent.spawn(download_tags, track, client)
                     for track in tracks
                     if client.is_in_uncrawled(track)]
    gevent.joinall(gevent_spawns)
    print(all_tags)

    # tracks = cPickle.load(open('tags', 'r'))
    # for track in tracks:
    #     get_tags(track)
