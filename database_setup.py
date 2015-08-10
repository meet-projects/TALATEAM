from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

#class profile(base):
#	id = profile.id
#	question = profile.question
#	oa = profile.oa
#	ob = profile.ob
#	oc = profile.oc
#	od = profile.od
#	oe = profile.oe
	
class User(Base):
	__tablename__ = 'user'
	name = User.name
	id = Column(Integer, primary_key=True)
	picURL = User.picURL
	username = Column(string)
	password = Column(string)

class Question(Base):
	option_a = Column(string)
	option_b = Column(string)
	option_c = Column(string)
	option_d = Column(string)
	text = Column(string)
	correct_option = Column(String) 
	Question_id = Coluomn(Integer, primary_key = True)
	user_id = User.id

class Q_response(Base):
	option_a = 0
	option_b = 0
	option_c = 0	
	option_d = 0
	Q_response_id = Column(Integer, prinamry_key = True)


#PLACE YOUR TABLE SETUP INFORMATION HERE

#gklsnlkbgse
