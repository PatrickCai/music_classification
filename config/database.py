import constants
import random

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Track(Base):
	__tablename__ = "track"

	id = Column(Integer, primary_key=True, autoincrement=True)
	username = Column(String(length=100))
	artist = Column(String(length=100))
	title = Column(String(length=100))
	test = Column(Enum(constants.DATA_TRAINING, constants.DATA_TEST, 
				constants.DATA_NOT_USED, constants.DATA_NOT_VALID))
	music_type = Column(Integer())


class Tag(Base):
	__tablename__ = "tag"

	id = Column(Integer, primary_key=True, autoincrement=True)
	track_id = Column(Integer)
	tag_type = Column(String(length=50))
	tag_value = Column(Integer())

def _get_session():
	engine = create_engine("mysql://root:@localhost/classification?charset=utf8", echo=False)
	Base.metadata.create_all(engine)
	Session = sessionmaker()
	Session.configure(bind=engine)
	session = Session()
	return session

def store_tag(artist, title, tag, value):
	session = _get_session()
	req_track = session.query(Track).filter(Track.title==title).filter(Track.artist==artist).first()
	if not req_track:
		return
	track_id = req_track.id 
	tag_instance = Tag(track_id=track_id, tag_type=tag, tag_value=value)
	session.add(tag_instance)
	req_track.test = constants.DATA_NOT_USED
	session.commit()

def store_track(username, artist, title):
	session = _get_session()
	track = Track(username=username, artist=artist, title=title)
	session.add(track)
	session.commit()

def fetch_track():
	session = _get_session()
	req_tracks = session.query(Track).filter(Track.test==constants.DATA_NOT_USED).filter(Track.music_type!=None).all()
	random.shuffle(req_tracks)
	train_number = int(len(req_tracks) * constants.TRAIN_TEST_RATIO)
	req_tracks = req_tracks[0: train_number]
	for req_track in req_tracks:
		req_track.test = constants.DATA_TRAINING
		session.commit()
	return req_tracks

def fetch_test_tracks():
	'''Get the tracks for testing'''
	session = _get_session()
	req_tracks = session.query(Track).filter(Track.test==constants.DATA_NOT_USED).filter(Track.music_type!=None).all()
	# for req_track in req_tracks:
	# 	req_track.test = constants.DATA_TEST
	# 	session.commit()
	return req_tracks

def fetch_tags():
	session = _get_session()
	tags_info = session.query(Tag).all()
	return tags_info

def restore_track_status():
	'''Restore the track status into NOT USED, if the track is labled with the music type'''
	session = _get_session()
	req_tracks = session.query(Track).filter(Track.music_type!=None).all()
	for req_track in req_tracks:
		req_track.test = constants.DATA_NOT_USED
		session.commit()

def fetch_one_track(track_id):
	session = _get_session()
	track_tags = session.query(Tag).filter(Tag.track_id==track_id).all()
	return track_tags

if __name__ == "__main__":
	# store_track('d', 'd', 'd')
	# store_tag('Destroyer','Kaputt','ele',1)
	# fetch_track()
	restore_track_status()
	# pass
