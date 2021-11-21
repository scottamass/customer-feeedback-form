from os import name
from flask import Flask, render_template ,request
from flask.scaffold import F
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///comments.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Int data base 

db=SQLAlchemy(app)

#users DB
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    user_name = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200))
#create db model

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    rating=db.Column(db.Integer)
    comments=db.Column(db.String(400), nullable=False)
 #   date_created = db.Column(db.DateTime, defult=datetime.utcnow)
#return a string when added
    def __init__(self,name ,rating,comments): 
        self.name = name
        self.rating = rating
        self.comments = comments


    def __repr__(self):
        return'<Name %r>' % self.name




@app.route("/", methods=['POST' , 'GET'])
@app.route("/home", methods=['POST' , 'GET'])
def hello():
    return render_template('index.html',c_name='Jumpstart')
    
@app.route("/submit", methods=['POST'])
def submit():
    if request.method =='POST':
        name = request.form['name']
        rating = request.form['options']
        comments = request.form['comments']
        
        
        # Push to DB
        
        new_customer = Comments(name=name, rating=rating, comments=comments)
        db.session.add(new_customer)
        db.session.commit()
        return f"thank you {name} {rating}"
        
        


      

#def form():
#    name_customer = request.form.get("customer")
#    rating = request.form.get("options")
#    return f"thank you {name_customer} {rating}"

@app.route("/js-admin")
def admin():
    feedback = Comments.query.order_by(Comments.id) 
    return render_template('admin.html' ,feedback=feedback ) 

if __name__ == '__main__':
    app.run  

    