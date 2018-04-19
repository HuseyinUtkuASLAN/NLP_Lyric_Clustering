import numpy as np

from feature_extract import filter_word, stem

def create_vector(data, feature_vector,class_list):
	
	vectors = []
	classes = []

	def find_index(word):
		for i,w in enumerate(feature_vector):
			if w == word:
				return i
		return None
	def find_cls_index(y):
		for i,c in enumerate(class_list):
			if c == y:
				return i
		print("ERROR. This class does not exist in the list!")
		quit()

	for words, y in data:
		vector = np.zeros([len(feature_vector)])
		c = np.zeros([len(class_list)])
		for w in words:
			count = words.count(w)
			frequency = count / len(words)
			assert frequency <= 1 and frequency >= 0,"frequency is bigger than 1 or smaller than 0"
			
			x_i = find_index(w)
			
			if x_i != None:
				assert x_i >= 0 and x_i < len(feature_vector), "index is smaller than 0 or bigger than size of feature vector i = {0}".format(str(x_i))

			vector[x_i] = frequency
		y = find_cls_index(y)
		c[y] = 1
		classes.append(c)
		vectors.append(vector)
	print("number of vectors created = {0}".format(str(len(vectors))))

	return np.array(vectors), np.array(classes)
