

#### 1. Text preprocessing (Taken from Codecademy.com")

1.0. noise removal := Removing unwanted data such as: 
			Punctuation and accents; 
			Special characters; 
			Numeric digits;
			Leading, ending, and vertival whitespace;
			HTML formatting

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


			=> you can apply the stemmer to word_tokenized strings with the highest effect
				applying it to sentences tokenized strings yields a low effect





	1.2.4. lemmatization := casting words to their root forms:

			this requires the method to know the part of speach for each word.

			applications: commonly used in search engines to better match user inputs with website hits.

			
			Implementation in Python:
			- NLTK's build-in lemmatizer called WordNetLemmatizer
					from nltk.stem import WordNetLemmatizer
					lemmatizer = WordNetLemmatizer()


			=> you can apply the lemmatizer to word_tokenized strings with low effect
				applying it to part of speech_tagged data yields best results



1.3 Part-of_speech Taggin:
                     It's about finding the part of speech for each word.
			A part-of-speech-tagging-funtion takes in a word and returns the most common aprt of speech for that word.

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

				.mmost_common returns a list of tuples each containing the word, the one position, the number of tiems this position is adopted in the set of synonims for that word.
				pos_counts.most_common(1)[0][0]

			4) define take the most common position as the most probable position:

				most_likely_part_of_speech = pos_counts.most_common(1)[0][0]

----------- ÜBERARBEITEN

2. Chunking:

2.1. patternmatching with regex in python:
	Implementation:
			- re.match("**pattern**", string)

2.2. grammar chunking with NLTK, is applied on tokenized part-of-speech tagged data. Rembemer, part of speech data is stored in lists where each token is stored in a tuple. The tuple contains the token and a tag for the most probable part-of-speech this token might be (tags are: NN for noun, JJ for adjective, and so on. for more info see:

	Implementation:
		from nltk import RegexpParser
		from pos_tagged_oz import pos_tagged_oz
		from np_chunk_counter import np_chunk_counter

		# for noun phrase
		chunk_grammar = "AN: {<JJ><NN>}"

		# for verb phrases there are two kinds
		chunk_grammar = "VP: {<VB.*><DT>?<JJ>*<NN><RN.?>?}"
		chunk_grammar = "VP: {<DT>?<JJ>*<NN><VB.*><RB.?>?}"

		# create a parser instance
		chunk_pareser = RegerexpParser(chunk_grammer)

		# implement the parser on tokenizer content of "pos_tagged_oz
		

2.3. Chunk filtering, works in two steps: Groups sentences into one chunk and after that (second) it excludes given patterns. The pattern for chunking sentences is notet in curly braces {}, meanwhile the patterns to exclude are note in inverted curly braces }{:

		Implementation:
from nltk import RegexpParser, Tree
from pos_tagged_oz import pos_tagged_oz

# define chunk grammar to chunk an entire sentence together
grammar = "Chunk: {<.*>+}"

# create RegexpParser object
parser = RegexpParser(grammar)

# chunk the pos-tagged sentence at index 230 in pos_tagged_oz
chunked_dancers = parser.parse(pos_tagged_oz[230])
print(chunked_dancers)

# define noun phrase chunk grammar using chunk filtering here
# filtering out verbal phrases we are left with noun phrases
chunk_grammar = """NP: {<.*>+}
                       }<VB.?|IN>+{"""

# create RegexpParser object here
chunk_parser = RegexpParser(chunk_grammar)

# chunk and filter the pos-tagged sentence at index 230 in pos_tagged_oz here
filtered_dancers = chunk_parser.parse(pos_tagged_oz[230])
print(filtered_dancers)

# pretty_print the chunked and filtered sentence here
Tree.fromstring(str(filtered_dancers)).pretty_print()


		
		