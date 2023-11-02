Defining a chatbot as a class

important concepts

intents :=

"actions the user ca perform through the  user"

utterances :=

"different statements of the user adressing one intent"

entities :=

"information a chatbot passes from the utterance to a triggered intent"


technical implementation of utterances, entities and intents into an instance variable witha  dictionary:

# for every intent and it's entity we define one key in the dictionary.
## Every intent has many possible corresponding utterances. But every key has only one value.
## So the value has to contain many different utterances related to one intent. This is implemented by saving as a value a list containing many different (regex) patterns of utterances adressing the intent.
## to get the entity from the user utterance, every (regex) pattern matching utterances contains a capture group, like "(\d+)". This capture group saves the information matched with the pattern in parentheses, to be later passed on to the intent
