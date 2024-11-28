import torch
import torch.nn as nn
from torchtyping import TensorType

class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        words = set() # To handle duplicates
        word_list = positive + negative
        for sentence in word_list:
            for word in sentence.split():
                words.add(word)

        sorted_list = sorted(list(words))
        mpp = {} # Dict for mapping word to integer 
        for i, c in enumerate(sorted_list):
            mpp[c] = i + 1 # Mapping starts from 1 

        def encode(sentence):
            integers = []
            for word in sentence.split():
                integers.append(mpp[word])
            return integers
        
        var_len_tensors = []
        for sentence in word_list:
            var_len_tensors.append(torch.tensor(encode(sentence)))
        
        return nn.utils.rnn.pad_sequence(var_len_tensors, batch_first = True)
