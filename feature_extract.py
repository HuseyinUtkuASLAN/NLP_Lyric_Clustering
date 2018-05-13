
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

class Extracted_info:

	def __init__(self, feature_vector, class_list, threshold, threshold_raw_value, mean,
		len_feature_vector_before_thresholding):
		self.feature_vector = feature_vector
		self.class_list = class_list
		self.threshold = threshold
		self.threshold_raw_value = threshold_raw_value
		self.mean = mean
		self.len_feature_vector_before_thresholding = len_feature_vector_before_thresholding

	def __str__(self):
		print(self.class_list)
		print("feature length before thresholding : ", self.len_feature_vector_before_thresholding)
		print("mean : " , self.mean)

		print("threshold raw : " , self.threshold_raw_value )
		print("threshold : " , self.threshold )

		print("feature length after thresholding : ", len(self.feature_vector))
		print("number of deleted features : ", self.len_feature_vector_before_thresholding - len(self.feature_vector) )

		return "\n"

def filter_word(text):
	stopWords = set(stopwords.words('english'))
	words = word_tokenize(text)
	wordsFiltered = []

	for w in words:
		if w not in stopWords:
			wordsFiltered.append(w)

	return wordsFiltered


def stem(wordsFiltered, st = PorterStemmer()):
	
	stemed = []
	for i,w in enumerate(wordsFiltered):
		stemed.append(st.stem(w))

	return stemed



def feature_extract(data, threshold = .3, st = PorterStemmer()):


	
	print("deleting stopwords, tokenizing words, stemming and creating feature vector ...\n")
	new_data = []
	class_list = []
	feature_vector = {}

	for d in data:
		# create class_list & pass "Not Available" 
		if d[1] == "Not Available" or d[1] == "Other":
			continue
		
		if d[1] not in class_list:
			class_list.append(d[1])

		wordsFiltered = filter_word(d[0])
		wordsFiltered = stem(wordsFiltered,st)
		new_data.append((wordsFiltered, d[1]))
		# print(wordsFiltered ,"\n\n")
		for word in wordsFiltered:
			if word not in feature_vector:
				feature_vector[word] = 1
			else:
				feature_vector[word] += 1
		

	print("thresholding {0} ...\n".format(str(threshold)))


	s = 0
	for f in feature_vector:
		s += feature_vector[f]

	threshold_raw_value = (s / len(feature_vector)) * threshold

	len_feature_vector_before_thresholding = len(feature_vector)

	tmp = dict(feature_vector)

	for f in feature_vector:
		if feature_vector[f] < threshold_raw_value:
			tmp.pop(f,None)
	feature_vector = tmp
	# print(feature_vector)
	# print(class_list)
	# print("feature length before thresholding : ", len_feature_vector_before_thresholding)
	mean = (s / len_feature_vector_before_thresholding)
	# print("mean : " ,  mean)

	# print("threshold : " , threshold_raw_value )

	# print("feature length after thresholding : ", len(feature_vector))
	# print("number of deleted features : ", len_feature_vector_before_thresholding - len(feature_vector) )

	info = Extracted_info(feature_vector, class_list, threshold, threshold_raw_value, mean,
		len_feature_vector_before_thresholding)

	return new_data, info
