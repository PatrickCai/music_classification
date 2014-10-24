#! /usr/bin/env python
# -- encoding:utf - 8 --
from config import constants, pylast
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_tags():
	network = pylast.LastFMNetwork(api_key = constants.API_KEY, api_secret = 
	    constants.API_SECRET)



def set_tags():
	pass

if __name__ == "__main__":
	get_tags()