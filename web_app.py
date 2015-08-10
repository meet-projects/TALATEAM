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

@app.route("/result/<int:user_id>/<int:result>", methods=['POST'])
def result(user_id, result):
	user = session.query(User).filter_by(id=user_id).first()
	return render_template("result.html", user=user, result=result)
	

@app.route("/profile/<int:user_id>/", methods=["GET", 'POST'])
def profilePage(user_id):
	user = session.query(User).filter_by(id=user_id).first()
	question=session.query(Question).filter_by(user_id=user.id).first()
	if request.method == 'GET':
		return render_template("profile.html", user=user, question=question)
	else:
		pass
		
	

@app.route('/')
def main():
	all_users = session.query(User).all()
	return render_template('main_page.html', users=all_users)
	




if __name__ == '__main__':
    app.run(debug=True)
