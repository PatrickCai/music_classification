#! /usr/bin/env python
# -- encoding:utf - 8 --

import sys
import cPickle

from config import database,constants

reload(sys)
sys.setdefaultencoding('utf-8')


# {"high": {"ambient": [0.1, 0.2, 0.4], "sad": [0, 0.3, 0.12]}, "middle":{"ambient": [0, 0.2, 0.5]}}
x_axis_percentage = cPickle.load(open("per_x", "r"))
y_axis_percentage = cPickle.load(open("per_y", "r"))
x_axis_type = cPickle.load(open("type_x", "r"))
y_axis_type = cPickle.load(open("type_y", "r"))


def test_one_track(track_id):
	raw_track_tags = database.fetch_one_track(track_id)	
	track_tags = dict(zip(constants.VALID_TAGS, 
					[ 0 for i in xrange(len(constants.VALID_TAGS))]))
	for raw_track_tag in raw_track_tags:
		track_tags[raw_track_tag.tag_type] = raw_track_tag.tag_value

	for emotion,tags_percentage in y_axis_type.iteritems():
		one_emotion_percentage = []
		tags_for = []
		for tag,index in track_tags.iteritems():
			perce = tags_percentage[tag][index]
			if perce == 0:
				one_emotion_percentage.append(constants.MIN_DUMMY)
			else:
				one_emotion_percentage.append(tags_percentage[tag][index])
			tags_for.append(tag)
		one_emotion_percentage.append(y_axis_percentage[emotion])
		print("%s : %s"%(emotion, one_emotion_percentage))
		print(tags_for)
		result = reduce(lambda x,y :x*y , one_emotion_percentage)
		print("%s : %s"%(emotion, result))






if __name__ == "__main__":
	test_one_track(1034)
