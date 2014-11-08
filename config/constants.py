API_KEY = "2e6e98ec329aa9c86bb8a541fc09bd29" # this is a sample key
API_SECRET = "c86c14938f3344707b0a56a0a1370e69"

#types for data (for training or test)
DATA_TRAINING = "Training"
DATA_TEST = 'Test'
DATA_NOT_USED = "Not used"
DATA_NOT_VALID = "Not valid"

#types of emotion in music
EMOTION_POSITIVE_NEUTRAL = 0
EMOTION_DYNAMIC = 1
EMOTION_POSITIVE_HIGH = 2
EMOTION_NEGATIVE_HIGH = 3
EMOTION_ANGER = 4
EMOTION_MELLOW = 5
EMOTION_SAD = 6
EMOTION_RELAXING = 7
EMOTION_AMBIENT = 8

EMOTIONS = [EMOTION_POSITIVE_NEUTRAL, EMOTION_DYNAMIC, EMOTION_POSITIVE_HIGH,
			EMOTION_NEGATIVE_HIGH, EMOTION_ANGER, EMOTION_MELLOW,
			EMOTION_SAD, EMOTION_RELAXING, EMOTION_AMBIENT]

X_AXIS_EMOTIONS = {"high":[1, 4], "up": [0, 2, 3], "down":[5, 6, 7],
				   "low": [8]}
Y_AXIS_EMOTIONS = {"happy": [1, 2, 7], "neutral": [0, 5], "sad": [3, 4, 6, 8]}

#list of valid tags
VALID_TAGS = ["ambient", "blues", "classic rock", "country", "dance",  "easy listening" , "emo" ,"folk", "gothic", "hip-hop", "minimal", "new wave", "noise", "piano", "post-punk", "post-rock", "psychedelic", "punk", "reggae", "Rnb", "shoegaze","singer-songwriter", "Ska" , "trip-hop", "Synthpop",
				"beautiful", "chillout", "cool", "melancholy", "Mellow", "sad","romantic", "saxophone", 'Lo-fi', 'summer', 'epic', 'calm']
TAGS_VALUE = ['1', '2']


#value to tell the track apart
MIDDLE_VALUE = 50
LOWEST_VALUE = 20

MIN_DUMMY = 1