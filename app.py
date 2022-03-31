from decimal import Decimal
from turtle import distance
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

app = Flask(__name__)

# change to name of your database; add path if necessary

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql11482395:3DHES1PgKK@sql11.freemysqlhosting.net/sql11482395'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

class Stats(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    strava_id = db.Column(db.Integer, nullable=False)
    acces_token = db.Column(db.String(50),nullable=False)
    refresh_token = db.Column(db.String(50), nullable=False)
    stats_id = db.Column(db.Integer, nullable=False)

class Stats1(db.Model):
    __tablename__ = 'activity'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(40),nullable=False)
    distance = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(10),nullable=False)

class Stats2(db.Model):
    __tablename__ = 'stats'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30),nullable=False)
    firstname = db.Column(db.String(20),nullable=False)
    lastname = db.Column(db.String(30),nullable=False)
    city = db.Column(db.String(40),nullable=False)
    state = db.Column(db.String(40),nullable=False)
    country = db.Column(db.String(40),nullable=False)
    sex = db.Column(db.String(4),nullable=False)
    profileimage = db.Column(db.Text(40),nullable=False)
       

#routes



@app.route('/')
def index():
    try:
        stats = Stats.query.order_by( desc(Stats.stats_id) ).all()
        stats1 = Stats1.query.order_by( desc(Stats1.id) ).all()
        stat_text = '<ul>'
        for stat in stats:
            stat_text += '<li>' + stat.acces_token + ', ' + str(stat.id) + '</li>'
        for sta in stats1:
            stat_text += '<li>' + str(sta.distance) + ', ' + sta.name + '</li>'
        stat_text += '</ul>'
        return stat_text
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

if __name__ == '__main__':
    app.run(debug=True)