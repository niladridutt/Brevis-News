# only need to be run once this will generate the following dir and files:
# vocab directory
# character_cnn.pt, word_embedding.pt, char_embedding.pt
# these are necessary for embedding_generator.py 

from allennlp.data.fields import TextField
from allennlp.data import Instance
from allennlp.data.token_indexers import SingleIdTokenIndexer, TokenCharactersIndexer
from allennlp.data.tokenizers import Token
from allennlp.data.vocabulary import Vocabulary
from allennlp.modules.token_embedders import Embedding, TokenCharactersEncoder
from allennlp.modules.text_field_embedders import TextFieldEmbedder, BasicTextFieldEmbedder
from allennlp.modules.seq2vec_encoders import CnnEncoder
from allennlp.data import Instance

import torch

# need a function which will return all the text in the dataset and save it to 'text' variable
#for now let us take this example 
text = "The Daman and Diu administration on Wednesday withdrew a circular that asked women staff to tie rakhis on male colleagues after the order triggered a backlash from employees and was ripped apart on social media.The union territory?s administration was forced to retreat within 24 hours of issuing the circular that made it compulsory for its staff to celebrate Rakshabandhan at workplace.?It has been decided to celebrate the festival of Rakshabandhan on August 7. In this connection, all offices/ departments shall remain open and celebrate the festival collectively at a suitable time wherein all the lady staff shall tie rakhis to their colleagues,? the order, issued on August 1 by Gurpreet Singh, deputy secretary (personnel), had said.To ensure that no one skipped office, an attendance report was to be sent to the government the next evening.The two notifications ? one mandating the celebration of Rakshabandhan (left) and the other withdrawing the mandate (right) ? were issued by the Daman and Diu administration a day apart. The circular was withdrawn through a one-line order issued late in the evening by the UT?s department of personnel and administrative reforms.?The circular is ridiculous. There are sensitivities involved. How can the government dictate who I should tie rakhi to? We should maintain the professionalism of a workplace? an official told Hindustan Times earlier in the day. She refused to be identified.The notice was issued on Daman and Diu administrator and former Gujarat home minister Praful Kodabhai Patel?s direction, sources said.Rakshabandhan, a celebration of the bond between brothers and sisters, is one of several Hindu festivities and rituals that are no longer confined of private, family affairs but have become tools to push politic al ideologies.In 2014, the year BJP stormed to power at the Centre, Rashtriya Swayamsevak Sangh (RSS) chief Mohan Bhagwat said the festival had ?national significance? and should be celebrated widely ?to protect Hindu culture and live by the values enshrined in it?. The RSS is the ideological parent of the ruling BJP.Last year, women ministers in the Modi government went to the border areas to celebrate the festival with soldiers. A year before, all cabinet ministers were asked to go to their constituencies for the festival."

words = text.split()
sentence = TextField([Token(x) for x in words], token_indexers={"tokens": SingleIdTokenIndexer(namespace="token_ids"), "characters": TokenCharactersIndexer(namespace="token_characters")})

instance = Instance({"sentence": sentence})
instances = [instance]

vocab = Vocabulary.from_instances(instances)

for instance in instances:
    instance.index_fields(vocab)

word_embedding = Embedding(num_embeddings=vocab.get_vocab_size("token_ids"), embedding_dim=10)
char_embedding = Embedding(num_embeddings=vocab.get_vocab_size("token_characters"), embedding_dim=5)
character_cnn = CnnEncoder(embedding_dim=5, num_filters=2, output_dim=8)

#saving everything
vocab.save_to_files("vocab")
torch.save(character_cnn, "character_cnn.pt")
torch.save(word_embedding, "word_embedding.pt")
torch.save(char_embedding, "char_embedding.pt")
