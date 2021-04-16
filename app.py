from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Initialize database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

# Initialize Authentication
app.config['SECRET_KEY'] = '7ZUXn;R}#tX3(9v' # 🚧 TODO: The secret key should be in a environment variable

login_manager = LoginManager() # initialize flask_login
login_manager.init_app(app) # initialize flask_login with our app
login_manager.login_view = 'signin' # redirect route when @login_required fails

# Connect flask login with the user records in our database:
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

# Models

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(50), unique=True)
  password = db.Column(db.String(80))
  is_admin = db.Column(db.Boolean, default=False)

# Routes

@app.route('/')
def index():
  if current_user.is_authenticated:
    # Show the home page only to logged in users:
    return render_template('index.html', email=current_user.email)
  else:
    # If users aren't logged in they should be redirected to the signin page:
    return redirect(url_for('signin'))


@app.route('/admin')
@login_required
def admin():
  if current_user.is_admin:
    return render_template('admin.html')
  else:
    return 'You are not authorized to view this page.'


@app.route('/signup', methods=['POST', 'GET'])
def signup():
  if request.method == 'POST':
    # Run this when submitting the signup form:
    try:
      # Assign form values to variables to make working with them easier later:
      email = request.form.get('email')
      password = request.form.get('password')
      password_confirmation = request.form.get('password_confirmation')
      # Checkboxes will send the string value. What we want for later is a boolean, though:
      is_admin = bool(request.form.get('is_admin'))

      # Validations: Throw an error if anything is wrong with the input parameters:
      if not email or not password:
        raise ValueError('Email or password parameter was missing.')

      if not password == password_confirmation:
        raise ValueError('The two passwords are not matching.')

      # Hash the password to be stored in the database in an encrypted format: 
      hashed_password = generate_password_hash(password, method='sha256')

      # Create a new use record in the database:
      new_user = User(email=email, password=hashed_password, is_admin=is_admin)
      # ⚠️ Note: The is_admin should normally not be part of a signup form but something set somwhere else in an app!
      db.session.add(new_user)
      db.session.commit()
      
      # Login the user
      login_user(new_user)

      # Send the user to the home page after successful login:
      return redirect('/')
    except Exception as error_message:
      # Rerender the signup page and display an error message if any of the code above failed:
      return render_template('signup.html', error="User could not be created. " + str(error_message))
  else:
    # Run this when a user goes too the /signup route in the browser:
    return render_template('signup.html')


@app.route('/signin', methods=['POST', 'GET'])
def signin():
  if request.method == 'POST':
    # Run this when submitting the signin form:
    try:
      # Assign form values to variables to make working with them easier later:
      email = request.form.get('email')
      password = request.form.get('password')
      # Checkboxes will send the string value. What we want for later is a boolean, though:
      remember = bool(request.form.get('remember'))

      # Try to find a user record in the database with the given email address:
      user = User.query.filter_by(email=email).first()

      # Make sure that the given password matches the encrypted password of the user from the database:
      if user and check_password_hash(user.password, password):
        # If the use exists and the encrypted password matches, login the user and send them to the home page:
        login_user(user, remember=remember)
        return redirect('/')
      else:
        # If no user with the given email address was found or the password doesn't match throw an error:
        raise ValueError('Could not login with given login parameters.')
    except:
      # Rerender the signin page with an error message if anything goes wrong in the code above:
      return render_template('signin.html', error="Invalid email or password.")
  else:
    # Run this when a user goes too the /signin route in the browser:
    return render_template('signin.html')


@app.route('/signout')
@login_required
def signout():
  # Logout users and send them back to the signin page:
  logout_user()
  return redirect(url_for('signin'))


# Run the server

if __name__ == "__main__":
  app.run(debug=True)