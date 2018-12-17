from allennlp.data.dataset import Batch
from allennlp.data.fields import TextField
from allennlp.data.instance import Instance
from allennlp.data.token_indexers.wordpiece_indexer import PretrainedBertIndexer
from allennlp.data.tokenizers import WordTokenizer
from allennlp.data.tokenizers.word_splitter import BertBasicWordSplitter
from allennlp.data.vocabulary import Vocabulary
from allennlp.modules.token_embedders.bert_token_embedder import PretrainedBertEmbedder
import re

tokenizer = WordTokenizer(word_splitter=BertBasicWordSplitter())
vocab = Vocabulary()
token_indexer = PretrainedBertIndexer('bert-base-uncased')
model = PretrainedBertEmbedder('bert-base-uncased')

class preprocessing(object):
  
    def __init__(self,text):
        self.text=text
    def bert_vector(self):
        words = re.split(r'\W+',self.text) 
        Text = ' '.join(words)
        
        tokens = tokenizer.tokenize(Text)
        
        instance = Instance({"tokens":TextField(tokens,{'bert':token_indexer})})
        batch = Batch([instance])
        batch.index_instances(vocab)
        
        padding_lenghts = batch.get_padding_lengths()
        tensor_dict = batch.as_tensor_dict(padding_lenghts)
        
        Tokens = tensor_dict["tokens"]
        
        bert_vectors = model(Tokens["bert"])
        return(bert_vectors)
