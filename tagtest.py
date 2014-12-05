import random
import cPickle

from config import pylast

API_KEY = "2e6e98ec329aa9c86bb8a541fc09bd29" # this is a sample key
API_SECRET = "c86c14938f3344707b0a56a0a1370e69"
network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = 
    API_SECRET)



# tags = ["ambient", "blues", "classic rock", "country", "dance",  "easy listening" , "emo" ,"folk", "gothic", "hip-hop", "minimal", "new wave", "noise", "piano", "post-punk", "post-rock", "psychedelic", "punk", "reggae", "Rnb", "shoegaze","sing-songwriter", "Ska" , "trip-hop", "Synthpop"]
# for tag in tags:
# 	real_tags = pylast.Tag(tag, network).get_similar()[0:4]
# 	for real_tag in real_tags:
# 		if real_tag.get_name() in tags:
# 			print("!!!!!!!!!!!!!!!!!two tags %s: %s"%(tag, real_tag))
# 	print("tag %s done"%(tag))

# track = pylast.Track('Gil Scott-Heron',"New York Is Killing Me", network)
# tags = track.get_top_tags()
# print(tags)

session_key = '1a91ae8be6dcc41774b952cb14246275'

network.session_key = session_key
user = network.get_authenticated_user()

# top_tracks = user.get_top_tracks(limit=100)
top_tracks = cPickle.load(open("top_tracks", "r"))
artists_frequency = {}

print(top_tracks)

# cPickle.dump(top_tracks, open("top_tracks", "w"))