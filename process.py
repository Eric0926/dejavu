from flask import Flask, render_template, request, jsonify
from search import vgg_search

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

	#image = request.form['image']
	name = request.form['name']

	if name:
		#results = vgg_search(image, 10)
		results = name

		return jsonify({'results' : name})

	return jsonify({'error' : 'Missing address!'})

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = '80')