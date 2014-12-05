#! /usr/bin/env python
# -- encoding:utf - 8 --
import cPickle
import sys
import random

from config import pylast, constants
reload(sys)
sys.setdefaultencoding('utf-8')

MAX_ARTIST_FREQUENCY = 4

network = pylast.LastFMNetwork(api_key=constants.API_KEY, api_secret=
                               constants.API_SECRET)
username = "patrickcai"
user = pylast.User(username, network)

print(user)
top_tracks = user.get_top_tracks(limit=2000)

print("Finished!")

artists_frequency = {}
selected_tracks = []

random.shuffle(selected_tracks)

for top_track in top_tracks:
    artist = top_track[0].artist
    artist_times = artists_frequency.get(artist, 0)
    if artist_times < MAX_ARTIST_FREQUENCY:
        selected_tracks.append(top_track)
        artists_frequency[artist] = artist_times + 1

random.shuffle(selected_tracks)

selected_tracks = selected_tracks[:800]

cPickle.dump(selected_tracks, open("top_tracks", "w"))

# print(top_tracks)
