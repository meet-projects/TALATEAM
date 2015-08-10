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
	name = "Miley Cyrus",
	picURL = "http://www.iluvcinema.in/hindi/wp-content/uploads/2014/08/Emraan-is-a-very-cool-person-Kay-Kay.jpg",
	id = 2
	)
	
	
	
		







