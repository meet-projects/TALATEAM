from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Person

engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()




Miley = User(
	name = "Miley Cyrus",
	id = 1,
	picURL = "http://cdni.condenast.co.uk/592x888/k_n/miley-cyrus_31jan14_getty_b_592x888.jpg",
	description = "description here"
	
	)
job = Question(
	option_a = "Teacher",
	option_b = "Singer",
	option_c = "Doctor",
	option_d = "Computer Engineer",
	text = "What is my job?",
	correct_option = "Singer", 
	id = 1,
	user_id = 1,
	user = relationship(User)
	)

Emraan = User(
	name = "Emraan Joe",
	id = 2,
	picURL = "http://www.iluvcinema.in/hindi/wp-content/uploads/2014/08/Emraan-is-a-very-cool-person-Kay-Kay.jpg",
	description = "description here"
	)
job = Question(
	option_a = "Teacher",
	option_b = "Singer",
	option_c = "Doctor",
	option_d = "Computer Engineer",
	text = "What is my job?",
	correct_option = "Singer", 
	id = 1,
	user_id = 2,
	user = relationship(User)
	)

David = User(
	name = "David Goliath",
	id = 3,
	picURL = "https://www.uiaa.org/calendar/viewphoto.asp?id=14237",
	description = "description here"
	)
job = Question(
	option_a = "Teacher",
	option_b = "Singer",
	option_c = "Doctor",
	option_d = "Computer Engineer",
	text = "What is my job?",
	correct_option = "Singer", 
	id = 1,
	user_id = 3,
	user = relationship(User)
	)

Joey = User(
	name = "Joey Green",
	id = 4,
	picURL = "http://usercontent2.hubimg.com/7505671_f260.jpg",
	description = "description here"
	)
job = Question(
	option_a = "Teacher",
	option_b = "Singer",
	option_c = "Doctor",
	option_d = "Computer Engineer",
	text = "What is my job?",
	correct_option = "Singer", 
	id = 1,
	user_id = 4,
	user = relationship(User)
	)

	
	
	
		







