# NLP_Lyric_Clustering


Purpose of this project is to cluseter songs by some variables and try to come up with somekind of a relationship between them. There are 3 parts

> **Before even start,** 
> 1. You need to add a folder to project. Name it "data_set" 
> 2. Download data from [kaggle](https://www.kaggle.com/gyani95/380000-lyrics-from-metrolyrics)
> 3. Move data to "data_set" folder

### Parts : 
1. **Info** : Display info about data and preprocess a little
2. **Feature Extraction** : by using tokenizer, stemmer, deleting stop words, tfidf method and LDA, we will create vectors to feed to the clustering algorithm
3. **Clustering** : By using k-means, we will try to cluster data

### Libraries needed to run:
1. NLTK
2. panda
3. numpy
4. sklearn

### Todo:
1. **MORE TESTS**
2. PCA can be added
3. Current error rate is 14%. This can be improved.
