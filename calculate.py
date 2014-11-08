#! /usr/bin/env python
# -- encoding:utf - 8 --

import sys
import cPickle

from config import database, constants

reload(sys)
sys.setdefaultencoding('utf-8')

def fetch_track_info():
	req_tracks = database.fetch_track()
	tracks_number = len(req_tracks)
	tracks_classification = {}	# {1: [12, 32], 2: [33, 45]},key->emotion id,,value list -> track ids
	for emotion in constants.EMOTIONS:
		emotion_tracks = [track.id for track in req_tracks if track.music_type==emotion]
		tracks_classification[emotion] = emotion_tracks
	return tracks_classification,tracks_number

def bl(number):
	return 100 * number


def classify_axis_emotion(axis, tracks):
	if axis == "x":
		axis_emotions = constants.X_AXIS_EMOTIONS
	elif axis == "y":
		axis_emotions = constants.Y_AXIS_EMOTIONS
	emotion_in_axis = {} #the type is similar to the tracks_classification
	for axis_emotion, track_ids in axis_emotions.iteritems():
		total_tracks = []
		for track_id in track_ids:
			total_tracks.extend(tracks[track_id])
		emotion_in_axis[axis_emotion] = total_tracks
	return emotion_in_axis

def _calculate_tags_percentage(track_ids, track_tags):
	'''计算tag出现频率'''
	tags_count = dict(zip(constants.VALID_TAGS, 
								[[0, 0, 0] for i in xrange(len(constants.VALID_TAGS))]))
	for track_id in track_ids:
		tags = [(track_tag.tag_type, track_tag.tag_value) for track_tag in track_tags
				if track_tag.track_id==track_id]
		value_tags = []
		for tag in tags:
			one_tag = tags_count[tag[0]] 
			tag_index = tag[1]
			one_tag[tag_index] += 1 #'summer': [3, 4, 1]
			value_tags.append(tag[0])
		#对于没有给出标签(也就是标签值为0)的tag
		remaining_tags = list(set(constants.VALID_TAGS)-set(value_tags))
		for remaining_tag in remaining_tags:
			tags_count[remaining_tag][0] += 1 
	#从个数到计算频率
	tags_percentage = {}
	for emotion, values in tags_count.iteritems():
		tags_percentage[emotion] = [float(bl(value)/len(track_ids)) for value in values]
	return tags_percentage

def calculate_probability(tracks_tags, emotion_in_axis):
	axis_type = {}
	for emotion, track_ids in emotion_in_axis.iteritems():
		tags_percentage = _calculate_tags_percentage(track_ids, tracks_tags)
		axis_type[emotion] = tags_percentage
	print(axis_type)
	return axis_type

def get_types_percentage(emotion_in_axis, tracks_number):
	axis_percentage = {}
	for emotion, tracks in emotion_in_axis.iteritems():
		axis_percentage[emotion] = float(bl(len(tracks))/tracks_number)
	print(axis_percentage)
	return axis_percentage

if __name__ == "__main__":
	tracks_classification,tracks_number = fetch_track_info()
	emotion_in_x_axis = classify_axis_emotion("x", tracks_classification)
	emotion_in_y_axis = classify_axis_emotion("y", tracks_classification)

	x_axis_percentage = get_types_percentage(emotion_in_x_axis, tracks_number)
	y_axis_percentage = get_types_percentage(emotion_in_y_axis, tracks_number)

	tracks_tags = database.fetch_tags()

	# {"high": {"ambient": [0.1, 0.2, 0.4], "sad": [0, 0.3, 0.12]}, "middle":{"ambient": [0, 0.2, 0.5]}}
	x_axis_type = calculate_probability(tracks_tags, emotion_in_x_axis)
	y_axis_type = calculate_probability(tracks_tags, emotion_in_y_axis)

	cPickle.dump(x_axis_percentage, open("per_x", "w"))
	cPickle.dump(y_axis_percentage, open("per_y", "w"))
	cPickle.dump(x_axis_type, open("type_x", "w"))
	cPickle.dump(y_axis_type, open("type_y", "w"))
	


