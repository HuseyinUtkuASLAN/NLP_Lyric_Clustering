import numpy as np
import pickle

from data import get_data
from feature_extract import feature_extract
from vectorize import create_vector
# ''' words filtering regarding to stop words in english '''

# ''' Stemming / game-gaming-gamed-games '''

# ''' feature vector or dictionary '''

# ''' preprocessing / tfidf '''

# ''' clustering / kMeans '''

extract = True
vectorize = True
n_samples = 380000

data = None
info = None
X = None
Y = None

# extract features
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
	data, info = feature_extract(data, threshold = .3)

	# somelist = [x for x in somelist if not determine(x)]

	# delete empty elements
	data = [x for x in data if not len(x[0]) == 0 ]

	file_info = open('info.obj', 'wb')
	file_data = open('data.obj', 'wb')
	pickle.dump(info,file_info)

	pickle.dump(data,file_data)

with open('info.obj', 'rb') as file:
	info = pickle.load(file)

# vectorize
if vectorize:
	with open('data.obj', 'rb') as file:
		data = pickle.load(file)

	print(info)
	print("number of data : ", len(data))

	X, Y = create_vector(data,info.feature_vector,info.class_list)
	
	np.save("X",X)
	np.save("Y",Y)


'''final touches'''
if type(X) != type(np.array([1])):
	X = np.load("X.npy")
if type(Y) != type(np.array([1])):
	Y = np.load("Y.npy")

if X.shape[0] == Y.shape[0]:
	print("Number of examples = {}\n".format(X.shape[0]))
else:
	print("Number of examples and classes does not match")
	print("n_examples : {}\tn_classes : {}".format(X.shape[0] , Y.shape[0]))
	quit()
print("---------- INFO ----------\n")
print(info)
print("--------------------------\n")


'''CLUSTERING'''
n_examples = int(X.shape[0])
n_clusters = 10
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=n_clusters, random_state=0, init = "random", max_iter = 10000000).fit(X[:n_examples])
# print(kmeans.labels_)

predicted = {}
for l in kmeans.labels_:
	if l not in predicted.keys():
		predicted[l] = 0
	predicted[l] += 1
print("-----predicted-----")
print(sorted(predicted.values()))
print("-------------------")

ys = {}
for l in Y:
	if l not in ys.keys():
		ys[l] = 0
	ys[l] += 1
print(sorted(ys.values()))