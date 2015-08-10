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
	name = Column(String)
	id = Column(Integer, primary_key=True)
	picURL = Column(String)
	description = Column(String)
	#username = Column(String)
	#password = Column(String)
	

class Question(Base):
	option_a = Column(String)
	option_b = Column(String)
	option_c = Column(String)
	option_d = Column(String)
	text = Column(String)
	correct_option = Column(String) 
	id = Column(Integer, primary_key = True)
	user_id = Column(Integer, ForeignKey("user.id"))
	user = relationship(User)

##class Q_response(Base):
	##counter_a = 0
	##option_b = 0
	##option_c = 0	
	##option_d = 0
	##Q_response_id = Column(Integer, primary_key = True)


#PLACE YOUR TABLE SETUP INFORMATION HERE

#gklsnlkbgse
