from flask import Flask, render_template, request, jsonify

import utils
import utils_vgg16
import utils_evaluation
from keras.applications.vgg16 import VGG16
import faiss
import sys

def vgg_search(img_url, nb_results):

    # load the index file
    index = faiss.read_index("Shiying_and_Jiwei_mini_index.index")

    # A VGG16 pre-trained model
    vgg16_model = VGG16(weights='imagenet', include_top=False)
    # vgg16_model.summary()

    # number of nearest neighbors for each descriptor
    k = 100

    #compute query vector of descriptors
    xq = utils_vgg16.eval_vgg_with_l2_norm_compute_xq_cloud(vgg16_model, img_url)

    if xq.shape == (0,):
        return None,None,None,None,None

    #actual search
    # xq - the descriptors of the query image
    # index - the whole index of the images in the storage
    # k - number of nearest neighbors for each descriptor
    # I - the indexes of the relevant similar images
    D, I = utils.search(xq, index, k)


    # Return top N file_ids (images' names) according to IC
    top_n, scores, sources = utils_evaluation.eval_retrieve_top_n(I, nb_results)

    numbers = list(range(1,11))

    #for num in numbers:
    #    print("Result number ", num, " is: ", top_n[num-1], " with score: ", scores[num-1])

    #with open("search_results.txt", "w") as f:
    #    for num in numbers:
    #        idx = str(top_n[num - 1])
    #        idx1 = idx[:3]
    #        idx2 = idx[3:]
    #        #https://storage.cloud.google.com/evaluation_images/111_14.jpg?authuser=2
    #        f.write("https://storage.cloud.google.com/evaluation_images/{}_{}.jpg\n".format(idx1, idx2))

    images = []
    for num in numbers:
        idx = str(top_n[num - 1])
        idx1 = idx[:3]
        idx2 = idx[3:]
        #https://storage.cloud.google.com/evaluation_images/111_14.jpg?authuser=2
        if idx1 != "444":
        	images.append("https://storage.cloud.google.com/evaluation_images/{}_{}.jpg\n".format(idx1, idx2))
        else:
        	images.append("https://storage.cloud.google.com/evaluation_images/{}_{}.png\n".format(idx1, idx2))

    return images

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

	image = request.form['name']
	print(image)
	print(type(image))

	if image:
		results = vgg_search(image, 10)

		return jsonify({'results' : results[0]})

	return jsonify({'error' : 'Missing address!'})

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = '80')
