from flask import Flask, render_template
app = Flask(__name__)

# SQLAlchemy stuff
from database_setup import Base, Person
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///crudlab.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


#YOUR WEB APP CODE GOES HERE








if __name__ == '__main__':
    app.run(debug=True)
