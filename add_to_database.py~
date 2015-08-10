from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, User, Question

engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()




Miley = User(
	name = "Miley Cyrus",
	picURL = "http://cdni.condenast.co.uk/592x888/k_n/miley-cyrus_31jan14_getty_b_592x888.jpg",
	description = "description here"
	
	)
mileyjob = Question(
	option_a = "Teacher",
	option_b = "Singer",
	option_c = "Doctor",
	option_d = "Computer Engineer",
	text = "What is my job?",
	correct_option = "Singer", 
	user_id = 1,
	counter_a = 0,
	counter_b = 0,
	counter_c = 0,
	counter_d = 0
	)

Emraan = User(
	name = "Emraan Joe",
	picURL = "http://www.iluvcinema.in/hindi/wp-content/uploads/2014/08/Emraan-is-a-very-cool-person-Kay-Kay.jpg",
	description = "description here"
	)
emraanjob = Question(
	option_a = "Teacher",
	option_b = "Singer",
	option_c = "Doctor",
	option_d = "Computer Engineer",
	text = "What is my job?",
	correct_option = "Singer", 
	user_id = 2,
	counter_a = 0,
	counter_b = 0,
	counter_c = 0,
	counter_d = 0
	)

David = User(
	name = "David Goliath",
	picURL = "https://www.uiaa.org/calendar/viewphoto.asp?id=14237",
	description = "description here"
	)
davidjob = Question(
	option_a = "Teacher",
	option_b = "Singer",
	option_c = "Doctor",
	option_d = "Computer Engineer",
	text = "What is my job?",
	correct_option = "Singer", 
	user_id = 3,
	counter_a = 0,
	counter_b = 0,
	counter_c = 0,
	counter_d = 0
	)

Joey = User(
	name = "Joey Green",
	picURL = "http://usercontent2.hubimg.com/7505671_f260.jpg",
	description = "description here"
	)
joeyjob = Question(
	option_a = "Teacher",
	option_b = "Singer",
	option_c = "Doctor",
	option_d = "Computer Engineer",
	text = "What is my job?",
	correct_option = "Singer", 
	user_id = 4,
	counter_a = 0,
	counter_b = 0,
	counter_c = 0,
	counter_d = 0)
session.add(Emraan)
session.add(Miley)
session.add(Joey)
session.add(emraanjob)
session.add(joeyjob)
session.add(mileyjob)
session.add(David)
session.add(davidjob)
session.commit()	
	
	
		







