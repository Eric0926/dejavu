from flask import Flask, render_template, request, jsonify
import search
from search import vgg_search

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():

	image = request.form['image']

	if image:
		results = vgg_search(image, 10)

		return jsonify({'results' : results})

	return jsonify({'error' : 'Missing address!'})

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = '80')