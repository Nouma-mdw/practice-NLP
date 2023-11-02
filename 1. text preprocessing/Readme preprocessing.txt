

#### 1. Text preprocessing (Taken from Codecademy.com")

1.0. noise removal := Removing unwanted data such as: 
			- HTML tags,
			- Punctuation and accents; 
			- Special characters; 
			- Numeric digits;
			- Leading, ending, and vertical whitespace;
			
		Noise is usually dependant on the source (API's, webscraping, or voice recognition.

		Implementation in Python:
			- re.sub('pattern', 'pattern_replacement', string_to_format) in Regex

1.1. tokenization := **identifying tokens, the single and smallest components of meaning
                     (letters are smaller components than words but have no meaning, that is why words are the smallest components of meaning)**

		Applications of tokenization are:
			- Finding how many words or sentences appear in text
			- Determining how many times a specific word or phrase exists
			- Accounting for which terms are likely to co-occour

		Tokens are usually words, but can also be sentences or other size pieces of text.
			
		Implementation in Python:
			- word_tokenize(string_to_format)
			- sent_tokenize(string_to_format)


1.2. normalization := is a catch-all term for different text preprocessing techniques like 
			- Upper or lowercasing
			- Stopword removal
			- Stemming := bluntly removing prefixes and suffixes from a word
			- Lemmatization := replacing a single_word token with its root

	1.2.1. upper. and lower case removal: using pythons build in string methods .lower() and .upper()
	
	1.2.2. Stopword removal : =
			Stopwords are usually the most common words in a language and don't provide any information 
				about the tone of a statement (e.g. 'a', 'an', 'the')
			Stopword removal is done, when we don't care about the sentence structure.

			Implementation in Python:
			- NLTK's built in library to create a set of stopwords:
					from nltk.corpus import stopwords
					stop_words = set(stopwords.words('english))
			- use tokenization and list comprehension to remove stopwords:
					nbc_statement '...'

					word_tokens = word_tokenize(nbc_statement)

					statement_no_stop = [word for word in word_tokens if word not in stop_words]
			

	1.2.3. stemming referrs to the removal of word affixes (prefixes and suffixes: e.g. stemming the word "going" would result in "go")
			applications: commonly used in search engines to better match user inputs with website hits.
			
			Implementation in Python:
			- NLTK's build-in stemmer called PorterStemmer
					from nltk.stem import PorterStemmmer
					stemmer = PorterStemmer()
				=> you can apply the stemmer to word_tokenized strings with the highest effect,
				applying it to sentence_tokenized strings yields a low effect


	1.2.4. lemmatization := casting words to their root forms:
			this requires the method to know the part of speach for each word.
			applications: commonly used in search engines to better match user inputs with website hits.
			
			Implementation in Python:
			- NLTK's build-in lemmatizer called WordNetLemmatizer
					from nltk.stem import WordNetLemmatizer
					lemmatizer = WordNetLemmatizer()
				# the lemmatize function treats every token as anoun, unless you pass the part_of_speech as a second argument: 
					lemmatized = [lemmatizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized]


			=> you can apply the lemmatizer to word_tokenized strings with low effect
				applying it to part_of_speech_tagged data yields best results



1.3 Part-of_speech Taggin:
                     It's about finding the part of speech (noun, verb, adjective or other) for each word.
			A part-of-speech-tagging-funtion takes in a word and returns the most common part of speech for that word.

Idea: 1) find a set of synonims of a word. 2) count how often a position (noun, verb, adjective) appears among all words in the the set of synonyms. 3) check for the  most common position 4) take the most common position of the set of synnonims as the most probable position for the target word

			Implementation in Python:
			1) find a set of synonims:

				from nltk.corpus import wordnet # importing a database on words
				wordnet.synsets(word)

			2) count positions for the set of  synonyms:

				from collections import Counter # importing a database on words
				pos_counts = Counter()

				pos_counts["n"] = len(  [ item for item in probable_part_of_speech if item.pos()=="n"]  )
				pos_counts["v"] = len(  [ item for item in probable_part_of_speech if item.pos()=="v"]  )
				pos_counts["a"] = len(  [ item for item in probable_part_of_speech if item.pos()=="a"]  )
				pos_counts["r"] = len(  [ item for item in probable_part_of_speech if item.pos()=="r"]  )
 			3) check for the  most common position:

				.mmost_common returns a list of tuples each containing the word, the one position, the number of items this position is adopted in the set of synonims for that word.
				pos_counts.most_common(1)[0][0]

			4) define take the most common position as the most probable position:

				most_likely_part_of_speech = pos_counts.most_common(1)[0][0]


#####Sources:
 - “Natural Language Processing with Python – Analyzing Text with the Natural Language Toolkit”, Steven Bird, Ewan Klein, and Edward Loper, Chapter 3. (https://www.nltk.org/book/ch03.html)

 - Video PLaylist "NLP with NLTK" (https://www.youtube.com/playlist?list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL)

 - 'Regular Expressions, Text Normalization, Edit Distance', Chapter 2 in "Speech and Language Processing" by Daniel Jurafsky & James H. Martin. (https://web.stanford.edu/~jurafsky/slp3/2.pdf)
