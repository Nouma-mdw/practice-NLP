'''Codecademy instructions
Context:
Gensim
Depending on the corpus of text we select to train a word embedding model, different word embeddings will be created according to the context of the words in the given corpus. The larger and more generic a corpus, however, the more generalizable the word embeddings become.

When we want to train our own word2vec model on a corpus of text, we can use the gensim package!

In previous exercises, we have been using pre-trained word embedding models stored in spaCy. These models were trained, using word2vec, on blog posts and news articles collected by the Linguistic Data Consortium at the University of Pennsylvania. With gensim, however, we are able to build our own word embeddings on any corpus of text we like.

To easily train a word2vec model on our own corpus of text, we can use gensim’s Word2Vec() function.

model = gensim.models.Word2Vec(corpus, size=100, window=5, min_count=1, workers=2, sg=1)

corpus is a list of lists, where each inner list is a document in the corpus and each element in the inner lists is a word token
size determines how many dimensions our word embeddings will include. Word embeddings often have upwards of 1,000 dimensions! Here we will create vectors of 100-dimensions to keep things simple.
don’t worry about the rest of the keyword arguments here!
To view the entire vocabulary used to train the word embedding model, we can use the .wv.vocab.items() method.

vocabulary_of_model = list(model.wv.vocab.items())

When we train a word2vec model on a smaller corpus of text, we pick up on the unique ways in which words of the text are used.

For example, if we were using scripts from the television show Friends as a training corpus, the model would pick up on the unique ways in which words are used in the show. While the generalized vectors in a spaCy model might not place the vectors for “Ross” and “Rachel” close together, a gensim word embedding model trained on Friends’ scripts would place the vectors for words like “Ross” and “Rachel”, two characters that have a continuous on and off-again relationship throughout the show, very close together!

To easily find which vectors gensim placed close together in its word embedding model, we can use the .most_similar() method.

model.most_similar("my_word_here", topn=100)

"my_word_here" is the target word token we want to find most similar words to
topn is a keyword argument that indicates how many similar word vectors we want returned
One last gensim method we will explore is a rather fun one: .doesnt_match().

model.doesnt_match(["asia", "mars", "pluto"])

when given a list of terms in the vocabulary as an argument, .doesnt_match() returns which term is furthest from the others.
Let’s play around with gensim word2vec models to explore the word embeddings defined on our own corpus of training data!


Instructions:
1.
As is common in so much of NLP, before we can do our fancy modeling we need to do some preprocessing!

In script.py we have lowercased and split the text of William Shakespeare’s Romeo and Juliet into a list of lists named romeo_and_juliet_processed, where each entry in the inner list is a word token of the play. All stop words, loaded from NLTK, have been removed as well.

Inspect the processed text by printing the first 20 entries of the inner list in romeo_and_juliet_processed to the terminal.

2.
Train a gensim word2vec model of 100 dimensions on romeo_and_juliet_processed using the same keyword arguments described in the narrative. Save your model to a variable named model.

3.
Save the vocabulary of your trained model as a list to a variable named vocabulary. Print vocabulary to the terminal and view it.

4.
Which words are used most similarly to “romeo” in Romeo and Juliet? Use .most_similar() to find the 20 most similar words to “romeo”, and save the result to a variable similar_to_romeo. Print similar_to_romeo to the terminal.

5.
Are “Romeo” and “Juliet” truly star crossed lovers? Let’s make sure!

Use .doesnt_match() to find which character in the below list is the odd-one-out, and save the result to a variable not_star_crossed_lover.

["romeo", "juliet", "mercutio"]

Print not_star_crossed_lover to the terminal.
'''

import gensim
from nltk.corpus import stopwords
from word2vec_gensim_romeo_juliet import romeo_and_juliet

# load stop words
stop_words = stopwords.words('english')

# preprocess text
romeo_and_juliet_processed = [[word for word in romeo_and_juliet.lower().split() if word not in stop_words]]

# view inner list of romeo_and_juliet_processed
print(romeo_and_juliet_processed[0][:20])

# train word embeddings model
model = gensim.models.Word2Vec(romeo_and_juliet_processed, size = 100, window = 5, min_count = 1, workers = 2, sg = 1)

# view vocabulary
vocabulary = list(model.wv.vocab.items())
# print(vocabulary)

# similar to romeo
similar_to_romeo = model.most_similar("romeo", topn=20)
print(similar_to_romeo)

# one is not like the others
not_star_crossed_lover = model.doesnt_match(["romeo", "juliet", "mercutio"])
print("This is not the star_crossed_lover: ", not_star_crossed_lover)