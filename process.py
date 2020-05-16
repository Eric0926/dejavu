from flask import Flask, render_template, request, jsonify
import search
from search import vgg_search

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

	name = request.form['name']

	if name:
		results = vgg_search(image, 10)
		result = results[0]

		return jsonify({'results' : result})

	return jsonify({'error' : 'Missing address!'})

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = '80')