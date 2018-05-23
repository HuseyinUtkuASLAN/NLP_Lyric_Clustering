import numpy as np
import pickle
import nltk

from plot import plot_clusters
from data import get_data
from feature_extract import feature_extract
from vectorize import create_vector
# ''' words filtering regarding to stop words in english '''

# ''' Stemming / game-gaming-gamed-games '''

# ''' feature vector or dictionary '''

# ''' preprocessing / tfidf '''

# ''' clustering / kMeans '''

extract = False
vectorize = True
n_samples = 10000
n_clusters = 2


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


	data = [x for x in data if int(x[2]) == 2009 and (x[1] == "Rock" or x[1] == "Pop" )  ]

	genres = {}
	for d in data:
		if d[1] not in genres.keys():
			genres[d[1]] = 0
		genres[d[1]] += 1

	print(genres)

	# suffle data
	# from random import shuffle
	# shuffle(data)


	# quit()
	data = data[:n_samples]

	'''extract data and save'''
	# data, info = feature_extract(data, threshold = 0.3,st = nltk.stem.SnowballStemmer('english'))
	data, info = feature_extract(data, threshold = 0.3)
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
n_examples = int(X.shape[0] * .9 )
print("Number of examples used during traning = {}".format(n_examples))

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=n_clusters, random_state=1, init = "random", max_iter = 100000).fit(X[:n_examples])
# print(kmeans.labels_)

predicted_Y = kmeans.predict(X[n_examples:])
print(predicted_Y)
predicted = {}
for i in range(0,10):
	predicted[i] = {}
	for j in range(0,10):
		predicted[i][j] = 0
Y_tmp = Y[n_examples:]

for i,pred in enumerate(predicted_Y):
	predicted[pred][Y[n_examples + i]] += 1 

plot_datas = []
for p in predicted.values():
	p = list(p.values())
	plot_datas.append(p)
	# print(p)


plot_clusters(plot_datas,N = 10,n_column = 2)

# predicted = {}
# for l in kmeans.labels_:
# 	if l not in predicted.keys():
# 		predicted[l] = 0
# 	predicted[l] += 1
# print("-----predicted-----")
# print(sorted(predicted.values()))
# print("-------------------")

# ys = {}
# for l in Y:
# 	if l not in ys.keys():
# 		ys[l] = 0
# 	ys[l] += 1
# print(sorted(ys.values()))



# python -i main.py