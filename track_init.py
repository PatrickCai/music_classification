#! /usr/bin/env python
# -- encoding:utf - 8 --
import cPickle
from config import constants,pylast,database
import sys

reload(sys)
sys.setdefaultencoding('utf-8')



def set_tracks():
	network = pylast.LastFMNetwork(api_key = constants.API_KEY, api_secret = 
	    constants.API_SECRET)

	username = "patrickcai"

	user = pylast.User(username, network)
	try:
		user.get_id()
	except pylast.WSError:
		print("Invalid user")
		exit()


	tracks = cPickle.load(open("top_tracks", "r"))
	for track in tracks:
		artist = unicode(track[0].artist)
		title = unicode(track[0].title)
		database.store_track(username, artist, title)

if __name__ == "__main__":
	set_tracks()