from flask import Flask, render_template
app = Flask(__name__)

# SQLAlchemy stuff
#from database_setup import Base, Person <--- Import your tables here!!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base
engine = create_engine('sqlite:///crudlab.db')
Base.metadata.creat_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


#YOUR WEB APP CODE GOES HERE
@app.route("/result/<int:person_id>/<int:result>", methods=['POST'])
def result(person_id, result):
	user = session.query(Person).filter_by(id=person_id).first()
	return render_template("result.html", user=user, result=result)
	

@app.route("/profile/<int:person_id>/", methods=["GET", 'POST'])
def profilePage(person_id):
	pass

@app.route('/')
def main():
    return render_template('main_page.html')





if __name__ == '__main__':
    app.run(debug=True)
