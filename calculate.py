#! /usr/bin/env python
# -- encoding:utf - 8 --

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

emotion_feature_types = {} # {"high": {"ambient": [0.1, 0.2, 0.4], "sad": [0, 0.3, 0.12]}, "middle":{"ambient": [0, 0.2, 0.5]}}
energy_feature_types = {}

def fetch_track_info():
	req_tracks = database.fetch_track()


def train_data():
	pass

def test_data():
	pass

if __name__ == "__main__":
	fetch_track_info()