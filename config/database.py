import constants

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
				constants.DATA_NOT_USED))
	music_type = Column(Enum(constants.EMOTION_DYNAMIC, constants.EMOTION_POSITIVE_HIGH,
							constants.EMOTION_NEGATIVE_HIGH, constants.EMOTION_ANGER,
							constants.EMOTION_MELLOW, constants.EMOTION_SAD,
							constants.EMOTION_RELAXING, constants.EMOTION_AMBIENT))

def store_track(username, artist, title):
	engine = create_engine("mysql://root:@localhost/classification?charset=utf8", echo=True)
	Base.metadata.create_all(engine)
	Session =sessionmaker()
	Session.configure(bind=engine)
	session = Session()
	track = Track(username=username, artist=artist, title=title)
	session.add(track)
	session.commit()

if __name__ == "__main__":
	store_track('d', 'd', 'd')