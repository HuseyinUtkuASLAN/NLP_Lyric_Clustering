import numpy as np
import pickle

from kmeans import kmeans, plot
from data import get_data
from feature_extract import feature_extract
from vectorize import create_vector
# ''' words filtering regarding to stop words in english '''

# ''' Stemming / game-gaming-gamed-games '''

# ''' feature vector or dictionary '''

# ''' preprocessing / term frequency - importance '''

# ''' clustering / kMeans '''

extract = False
vectorize = False
n_samples = 200

data = None
info = None
X = None
Y = None


if extract:

	'''Load data'''
	data_name = "380000"

	print("loading data {0} ...\n".format(data_name))

	data = get_data(data_name)

	
	# suffle data
	from random import shuffle
	shuffle(data)

	data = data[:n_samples]

	'''extract data and save'''
	data, info = feature_extract(data)

	file_info = open('info.obj', 'wb')
	file_data = open('data.obj', 'wb')
	pickle.dump(info,file_info)

	pickle.dump(data,file_data)

with open('info.obj', 'rb') as file:
	info = pickle.load(file)

if vectorize:
	with open('data.obj', 'rb') as file:
		data = pickle.load(file)

	print(info)
	print("number of data : ", len(data))

	X, Y = create_vector(data,info.feature_vector,info.class_list)
	
	np.save("X",X)
	np.save("Y",Y)
	# file_X = open('X', 'wb')
	# file_Y = open('Y', 'wb')
	# pickle.dump(X,file_X)
	# pickle.dump(Y,file_Y)

# with open('X', 'rb') as file:
# 	X = pickle.load(file)
# with open('Y', 'rb') as file:
# 	Y = pickle.load(file)
X = np.load("X.npy")
Y = np.load("Y.npy")
print("number of X = {0}".format(X.shape))
print("number of Y = {0}".format(Y.shape))
kmeans(Y[0].shape[0], X)
# prototypes, history_centroids, belongs_to = kmeans(Y[0].shape[0], X)
# plot(X, history_centroids, belongs_to)
# import random
# rnd = random.randint(0, len(data)-1)
# filtered = filter_word(data[rnd][0])
# print(stem(filtered), "\t", data[rnd][1])