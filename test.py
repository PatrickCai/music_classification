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


def _to_percentage(emotion_result):
	total = sum(emotion_result.values())
	results = {}
	for emotion, value in emotion_result.iteritems():
		results[emotion] = float(value/total)
	return results

def test_one_track(track_id, axis):
	if axis == "x":
		axis_type = x_axis_type
		axis_percentage = x_axis_percentage
	elif axis == "y":
		axis_type = y_axis_type
		axis_percentage = y_axis_percentage

	raw_track_tags = database.fetch_one_track(track_id)	
	track_tags = dict(zip(constants.VALID_TAGS, 
					[ 0 for i in xrange(len(constants.VALID_TAGS))]))
	for raw_track_tag in raw_track_tags:
		track_tags[raw_track_tag.tag_type] = raw_track_tag.tag_value

	emotion_result = {}
	for emotion,tags_percentage in axis_type.iteritems():
		one_emotion_percentage = []
		for tag,index in track_tags.iteritems():
			perce = tags_percentage[tag][index]
			if perce == 0:
				one_emotion_percentage.append(constants.MIN_DUMMY)
			else:
				one_emotion_percentage.append(tags_percentage[tag][index])
		one_emotion_percentage.append(axis_percentage[emotion])
		result = reduce(lambda x,y :x*y , one_emotion_percentage)
		emotion_result[emotion] = result
	emotion_result = _to_percentage(emotion_result)
	# {"High": 0.2, "up" : 0.6, "down": 0.1, "low": 0.3}
	print(emotion_result)
	return emotion_result

def calculate_success_percentage(track, emotion_result, axis, success_count):
	music_type = track.music_type
	emotion = sorted(emotion_result.items(), key=lambda x:x[1], reverse=True)[0][0]
	print("The track is %s - %s"%(track.artist, track.title))
	
	print("The music type is %s"%(music_type))
	print("The x emotion is %s"%(emotion))
	if axis == "x":
		music_types = constants.X_AXIS_EMOTIONS[emotion]
	elif axis == "y":
		music_types = constants.Y_AXIS_EMOTIONS[emotion]

	if music_type in music_types:
		print("RIGHT!")
		success_count += 1
		print(success_count)
	else:
		print("WRONG!")
	print("*******************")
	return success_count

if __name__ == "__main__":
	tracks = database.fetch_test_tracks()
	success_count = 0
	for track in tracks:
		x_emotion_result = test_one_track(track.id, "x")
		success_count = calculate_success_percentage(track, x_emotion_result, "x", success_count)

		# y_emotion_result = test_one_track(track.id, "y")
		# success_count = calculate_success_percentage(track, y_emotion_result, "y", success_count)
	print(len(tracks))	
	print("The success percentage is %s"%(100 * success_count/len(tracks)))


