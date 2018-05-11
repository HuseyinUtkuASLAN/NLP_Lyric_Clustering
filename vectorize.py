import numpy as np
import pickle

from feature_extract import filter_word, stem

def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    # print(wordDict)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bowCount)
    return tfDict

def computeIDF(docList):
    import math
    N = len(docList)
    #divide N by denominator above, take the log of that
    for word, val in docList.items():
        docList[word]= math.log(N / float(val)) 

    return docList

def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val * idfs[word]
    return tfidf

def create_vector(data, feature_vector, class_list):

	def find_cls_index(y):
		for i,c in enumerate(class_list):
			if c == y:
				return i
		print("ERROR. This class does not exist in the list!")
		quit()


	vectors = []
	classes = []
	for text,c in data:
		if(len(text) == 0):
				raise AttributeError("text is empty")
		
		# create y

		c = find_cls_index(c)
		classes.append(c)

		# create vectors to feed tfidf
		vector = dict.fromkeys(feature_vector,0)
		for w in text:
			if w in feature_vector:
				vector[w] += 1
		vectors.append(vector)



	tfidfs = []

	# calculate tfidfs 
	idfs = computeIDF(feature_vector)

	for i in range(0,len(data)):
		tf = computeTF(vectors[i],data[i][0])
		tfidf = computeTFIDF(tf,idfs)
		tfidfs.append(np.array(list(tfidf.values())))

	# X and Y // numpy arrays
	return np.array(tfidfs), np.array(classes)



# lunch extract before this script
if __name__=="__main__":
	

	with open('info.obj', 'rb') as file:
		info = pickle.load(file)

	with open('data.obj', 'rb') as file:
		data = pickle.load(file)

	print(info)
	print("number of data : ", len(data))

	X,Y = something_something_dark_side(data,info.feature_vector,info.class_list)

	for i in range(0,1):
		print(data[i][0], X[i])

	# # print(data[0])

	# # X, Y = create_vector(data,info.feature_vector,info.class_list)

	# # print(info.feature_vector)

	# # vector = dict.fromkeys(info.feature_vector,0)
	# vectors = []
	# for text,_ in data:
	# 	vector = dict.fromkeys(info.feature_vector,0)
	# 	for w in text:
	# 		if w in info.feature_vector:
	# 			vector[w] += 1
	# 	vectors.append(vector)



	# tfidfs = []

	# # calculate tfidfs 
	# idfs = computeIDF(info.feature_vector)

	# for i in range(0,len(data)):
	# 	if(len(data[i][0]) == 0):
	# 		raise AttributeError("text is empty")
	# 	tf = computeTF(vectors[i],data[i][0])
	# 	tfidf = computeTFIDF(tf,idfs)
	# 	tfidfs.append(np.array(list(tfidf.values())))




	# # tf = computeTF(vector,data[0][0])
	# # # print(tf)
	# # idfs = computeIDF(info.feature_vector)
	# # # print(info.feature_vector)

	# # tfidf = computeTFIDF(tf,idfs)
