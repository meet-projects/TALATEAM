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
	picURL = "http://cdni.condenast.co.uk/592x888/k_n/miley-cyrus_31jan14_getty_b_592x888.jpg",
	id = 1
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
	picURL = "http://www.iluvcinema.in/hindi/wp-content/uploads/2014/08/Emraan-is-a-very-cool-person-Kay-Kay.jpg",
	id = 2
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
	picURL = "https://www.uiaa.org/calendar/viewphoto.asp?id=14237",
	id = 3
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
	picURL = "http://usercontent2.hubimg.com/7505671_f260.jpg",
	id = 3
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

	
	
	
		







