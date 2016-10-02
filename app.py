from flask import *
from flask_pymongo import PyMongo
from data_controller import *
import os , time

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['MONGO_DBNAME'] = 'psthis'
app.config['MONGO_URI'] = 'mongodb://siromerm:qwertygg@ds051980.mlab.com:51980/psthis'
mongo = PyMongo(app)

@app.route('/register' , methods=['POST','GET'])
def register():
	if request.method == 'POST':
		register_data = {}
		register_data ['gems'] = 0
		register_data ['score'] = 0
		register_data ['email'] = request.form['email']
		register_data ['password'] = request.form['password']
		register_data ['name'] = request.form['user_name']
		register_data ['about'] = request.form['about_me']
		if register_check(register_data):
			register_controller(mongo , register_data)
			session['username'] = register_data['name']
			return redirect(url_for('home'))
		else:
			return render_template('register.html' , error_text = "Try another name")

	if request.method == 'GET':
		return render_template("register.html")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload' , methods=['POST','GET'])
def upload():

	image_name = request.form['image_name']
	uploader = request.form['uploader']
	link = request.form['link']
	description = request.form['description']
	tags = request.form['tags']
	done = 0
	price = request.form['price']
	save_location = "/images/" + int(round(time.time() * 1000))
	return render_template('upload.html')

if __name__ == "__main__":
	app.run(debug=True)
