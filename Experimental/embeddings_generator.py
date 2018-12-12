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
import numpy

vocab = Vocabulary.from_files("vocab")

character_cnn = torch.load("character_cnn.pt")
word_embedding = torch.load("word_embedding.pt")
char_embedding= torch.load("char_embedding.pt")

def get_embeddings(text):
    words = text.split()
    sentence = TextField([Token(x) for x in words], token_indexers={"tokens": SingleIdTokenIndexer(namespace="token_ids"), "characters": TokenCharactersIndexer(namespace="token_characters")})
    
    instance = Instance({"sentence": sentence})
    instances = [instance]
    for instance in instances:
        instance.index_fields(vocab)
    
    batch = Batch(instances)
    tensors = batch.as_tensor_dict(batch.get_padding_lengths())
    
    text_field_variables = tensors["sentence"]
    
    # This will have shape: (batch_size, sentence_length, word_embedding_dim + character_cnn_output_dim)
    embedded_text = text_field_embedder(text_field_variables)
    return embedded_text
