from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# SQLAlchemy stuff

#from database_setup import Base, user <--- Import your tables here!!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base
engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


#YOUR WEB APP CODE GOES HERE
@app.route('/')
@app.route('/profiles')
def main():
	all_users = session.query(User).all()
	return render_template('main_page.html', users=all_users)

@app.route('/profiles/<int:profile_id>')
def viewProfile(profile_id):
		
	user = session.query(User).filter_by(id = profile_id).first()
	#Get the Question for that user	
	return render_template('profile.html')

@app.route

if __name__ == '__main__':
    app.run(debug=True)
