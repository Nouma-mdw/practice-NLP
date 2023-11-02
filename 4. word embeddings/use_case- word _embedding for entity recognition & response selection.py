# main idea: recognize user_message_entities suited to fill in blank_spaces from selected response_candidate - in the style of "mad lib".

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import spacy
word2vec = spacy.load('en')

message_nouns = [ 'weekend', 'package','shirts']

#define `tokens` and `category`below
category = word2vec("clothes")
tokens = word2vec((" ").join(message_nouns))

def compute_similarity(tokens, category):
  output_list = list()
  #your code here
  for token in tokens:
    output_list.append(f"{token.text} {category.text} {token.similarity(category)}")

  return output_list

# print(compute_similarity(tokens, category))

# blank_spot = message_nouns[0]
# bot_response = f"Hey! I just checked my records, your shipment containing {blank_spot} is en route. Expect it within the next two days!"
# print(bot_response)

# ALTERNATE SOLUTION

blank_spot = "clothes"
category = word2vec(blank_spot)

message_noun_embeddings = list()
for noun in message_nouns:
  message_noun_embeddings.append(word2vec(noun))

def compute_similarity_value(target_token_spacy, similarity_candidates_list):
  output_list = list()
  for token in similarity_candidates_list:
    output_list.append(target_token_spacy.similarity(token))
  return np.array(output_list)

similarity_values = compute_similarity_value(category, message_noun_embeddings)

print(similarity_values)

sim_noun_index = similarity_values.argmax()
print("Sim_noun_index \n", sim_noun_index)

blank_spot = message_nouns[sim_noun_index]
bot_response = f"Hey! I just checked my records, your shipment containing {blank_spot} is en route. Expect it within the next two days!"
print(bot_response)