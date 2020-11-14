from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"



db = SQLAlchemy(app)

class USER(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))

@app.route('/<name>/<location>')
def index(name, location):
    user = USER(name=name, location=location)
    db.session.add(user)
    db.session.commit()
    return '<h1> Added New User </h1>'

@app.route('/')
def filter():
    members = USER.query.all()
    
    #members = USER.query.filter_by(name = 'Ahmed')
    return render_template('filter.html', members = members)

@app.route('/guestbook')
def guestbook():
    return render_template("guestbook.html") 

@app.route("/livesearch", methods=["POST", "GET"]) 
def livesearch():
    searchbox = request.form.get("text")
    print(searchbox)
    x =[{"name": "John","age": 30,"city": "New York"}, {"name": "ahemd","age": 40,"city": "York"}]
    return jsonify(x)
    
   

if __name__ == '__main__':
    app.run(debug=True, port=5000)