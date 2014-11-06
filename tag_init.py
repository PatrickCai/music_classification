#! /usr/bin/env python
# -- encoding:utf - 8 --
import sys
import cPickle
import gevent
from gevent import monkey
monkey.patch_all()

from config import constants, pylast, database
reload(sys)
sys.setdefaultencoding('utf-8')

tracks = cPickle.load(open("top_tracks", "r"))

# tracks = tracks[81:82]

tag_value = []

all_tags = [] # each element [(artist, title), tags]


def get_tags(track):
	tags = track[1]
	for tag in tags:
		if str(tag[0]) in constants.VALID_TAGS:
			if int(tag[1]) < constants.MIDDLE_VALUE:
				value = 1
			else :
				value = 2
			artist = str(track[0][0])
			title = str(track[0][1])
			tag = str(tag[0])
			database.store_tag(artist, title, tag, value)


def download_tags(track):
	tags = track[0].get_top_tags()
	tag = [(track[0].artist, track[0].title), tags]
	all_tags.append(tag)
	print(len(all_tags))
	cPickle.dump(all_tags, open('tags', 'w'))


if __name__ == "__main__":
	# gevent_spawns = [gevent.spawn(download_tags, track) for track in tracks]
	# gevent.joinall(gevent_spawns)
	# print(all_tags)

	tracks = cPickle.load(open('tags', 'r'))
	for track in tracks:
		get_tags(track)
