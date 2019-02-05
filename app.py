""" Main server file for the application."""

# Importing the libraries
from flask import Flask, render_template, request
# for security precautions cors library
from flask_cors import CORS

# Import models
from models import create_post, get_posts

# Server object
app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		pass

	if request.method == 'POST':
		name = request.form.get('name')
		post = request.form.get('post')

		create_post(name, post)

	posts = get_posts()

	return render_template('index.html', posts=posts)



# Run the server on localhost on port 80 with debug mode on
if __name__ == '__main__':
	app.run(host='localhost', port='80', debug=True)