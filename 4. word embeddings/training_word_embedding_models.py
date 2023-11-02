'''Codecademy instructions
Context:
Word2vec
You might be asking yourself a question now. How did we arrive at the vector values that define a word vector? And how do we ensure that the values chosen place the vectors for words with similar context close together and the vectors for words with different usages far apart?

Step in word2vec! Word2vec is a statistical learning algorithm that develops word embeddings from a corpus of text. Word2vec uses one of two different model architectures to come up with the values that define a collection of word embeddings.

One method is to use the continuous bag-of-words (CBOW) representation of a piece of text. The word2vec model goes through each word in the training corpus, in order, and tries to predict what word comes at each position based on applying bag-of-words to the words that surround the word in question. In this approach, the order of the words does not matter!

The other method word2vec can use to create word embeddings is continuous skip-grams. Skip-grams function similarly to n-grams, except instead of looking at groupings of n-consecutive words in a text, we can look at sequences of words that are separated by some specified distance between them.

For example, consider the sentence "The squids jump out of the suitcase". The 1-skip-2-grams includes all the bigrams (2-grams) as well as the following subsequences:

(The, jump), (squids, out), (jump, of), (out, the), (of, suitcase)

When using continuous skip-grams, the order of context is taken into consideration! Because of this, the time it takes to train the word embeddings is slower than when using continuous bag-of-words. The results, however, are often much better!

With either the continuous bag-of-words or continuous skip-grams representations as training data, word2vec then uses a shallow, 2-layer neural network to come up with the values that place words with a similar context in vectors near each other and words with different contexts in vectors far apart from each other.

Let’s take a closer look to see how continuous bag-of-words and continuous skip-grams work!


Instructions:
1.
At the top of script.py you’ll find the opening sentence of Charles Dickens’s novel A Tale of Two Cities, stored in a variable sentence. Below, you’ll see that this sentence has been preprocessed for you and saved as sentence_lst.

You’ll also find a function called get_cbows() that we’ve defined. get_cbows() iterates through a preprocessed sentence word by word and returns a list of the different bag-of-words representations for the context words that surround each word in the sentence.

In the area indicated in script.py, call get_cbows() with sentence_lst and context_length as arguments, and save the result to a variable cbows.

What do you see printed to the terminal? Open the hint for an explanation of the output.

2.
Also provided in script.py is a function called get_skip_grams(). get_skip_grams() iterates through a sentence word by word and returns an ordered list of the different context words that surround each word in the sentence.

In the area indicated in script.py, call get_skip_grams() with sentence_lst and context_length as arguments, and save the result to a variable skip_grams.

What do you see printed to the terminal? How do these results differ from the previous exercise’s results? Open the hint for an explanation of the output.

3.
Above the functions in script.py we currently have a variable context_length set to 2. This indicates that when finding our bag-of-words and skip-gram representations, we are only looking 2 words to the left and 2 words to the right of our word we are focusing on.

Update the value of context_length to 3. How do the bag-of-words and skip-gram representations change?
'''

from sklearn.feature_extraction.text import CountVectorizer

sentence = "It was the best of times, it was the worst of times."
print(sentence)

# preprocessing
sentence_lst = [word.lower().strip(".") for word in sentence.split()]

# set context_length
context_length = 3

# function to get cbows
def get_cbows(sentence_lst, context_length):
  cbows = list()
  for i, val in enumerate(sentence_lst):
    if i < context_length:
      pass
    elif i < len(sentence_lst) - context_length:
      context = sentence_lst[i-context_length:i] + sentence_lst[i+1:i+context_length+1]
      vectorizer = CountVectorizer()
      vectorizer.fit_transform(context)
      context_no_order = vectorizer.get_feature_names()
      cbows.append((val,context_no_order))
  return cbows, #f"This is vectorizer.vocabulary_{vectorizer.vocabulary_}"

# define cbows here:
cbows = get_cbows(sentence_lst, context_length)

# function to get cbows
def get_skip_grams(sentence_lst, context_length):
  skip_grams = list()
  for i, val in enumerate(sentence_lst):
    if i < context_length:
      pass
    elif i < len(sentence_lst) - context_length:
      context = sentence_lst[i-context_length:i] + sentence_lst[i+1:i+context_length+1]
      skip_grams.append((val, context))
  return skip_grams

# define skip_grams here:
skip_grams = get_skip_grams(sentence_lst, context_length)

try:
  print('\nContinuous Bag of Words')
  for cbow in cbows:
    print(cbow)
except:
  pass
try:
  print('\nSkip Grams')
  for skip_gram in skip_grams:
    print(skip_gram)
except:
  pass