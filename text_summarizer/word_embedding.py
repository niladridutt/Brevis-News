from allennlp.data.dataset import Batch
from allennlp.data.fields import TextField
from allennlp.data.instance import Instance
from allennlp.data.token_indexers.wordpiece_indexer import PretrainedBertIndexer
from allennlp.data.tokenizers import WordTokenizer
from allennlp.data.tokenizers.word_splitter import BertBasicWordSplitter
from allennlp.data.vocabulary import Vocabulary
from allennlp.modules.token_embedders.bert_token_embedder import PretrainedBertEmbedder

class preprocessing(object):
  
    def __init__(self,text):
        self.text=text
    def word_embeddings(self):
        words = re.split(r'\W+',self.text) 
        Text = ' '.join(words)
        
        tokenizer=WordTokenizer(word_splitter=BertBasicWordSplitter())
        
        tokens = tokenizer.tokenize(Text)
        vocab = Vocabulary()
        token_indexer = PretrainedBertIndexer('bert-base-uncased')
        
        instance = Instance({"tokens":TextField(tokens,{'bert':token_indexer})})
        batch = Batch([instance])
        batch.index_instances(vocab)
        
        padding_lenghts = batch.get_padding_lengths()
        tensor_dict = batch.as_tensor_dict(padding_lenghts)
        
        Tokens = tensor_dict["tokens"]
        
        model = PretrainedBertEmbedder('bert-base-uncased')
        bert_vectors = model(Tokens["bert"])
        return(bert_vectors)