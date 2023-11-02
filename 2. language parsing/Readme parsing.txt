Parsing:=
breaking text into parts according to syntax

- part of speeach tagging
- n-grams
- Named Entity recognition (NER) to recognize  words like (Natalia or Berlin)



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


sources:

- Natural language processing with python chapter 7 (https://www.nltk.org/book/ch07.html)


		
		