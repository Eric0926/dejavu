from flask import Flask, render_template, request, jsonify
import search
from search import vgg_search

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

	image = request.form['image']

	if image:
		#results = vgg_search(image, 10)
		results = ["lalala"]

		return jsonify({'results' : results})

	return jsonify({'error' : 'Missing address!'})

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = '80')