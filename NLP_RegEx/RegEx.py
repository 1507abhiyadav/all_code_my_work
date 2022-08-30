from ast import pattern
from dataclasses import replace
import re
import string
import token
from unittest import result


###### Match Function
# string = "Tiger is the national animal of india"
# pattern ="Tiger"
# result = re.match(pattern,string)
# print(result.group(0))        
## output = Tiger

### Search Function###
# string = "Tiger is the national animal of india"
# pattern = "national"
# result = re.search(pattern,string)  # print == <re.Match object; span=(13, 21), match='national'>
# print(result.group(0))
### output -- national

### Findall function ###########
# string = "national animal is tiger and national sport is hockey"
# pattern = "national"
# result = re.findall(pattern,string)
# print(result)
### output -- ['national', 'national']


# ### Finditer function ###########
# string = "national animal is tiger and national sport is hockey"
# pattern = "national"
# result = re.finditer(pattern,string)
# # print(result)###   <callable_iterator object at 0x00000279F7407D60> 
# for res in result:
#     # print(res) ###   <re.Match object; span=(0, 8), match='national'> <re.Match object; span=(29, 37), match='national'>
#     print(res.start()) 
# ### output -- 0  29


### date function ####
# string = 'abhi23 15-07-1999, abh233 16-07-1999'
# pattern = r'\d{2}-\d{2}-\d{4}' ## d --> number(digit) , {}--> number of digit
### pattern = \d{2}-\d{2}-\d{4}
# result = re.findall(pattern,string)
# print(result)
# #### output --- ['15-07-1999', '16-07-1999']

# ###  split function  #####
# string = "this is a sample text string"
# pattern = r'[\s]'##  r'[,\s]'     r'[;,\s]'
# result = re.split(pattern,string)
# print(result)
# #### output -->['this', 'is', 'a', 'sample', 'text', 'string']


# ### sub function  #####
# string = "Cricket is a popular sport of india"
# pattern ="india"
# replace = "the world"
# result = re.sub(pattern,replace,string)
# print(result)
# ### output --->  Cricket is a popular sport of the world



################# Tokenization  ##################
#from nltk.tokenize import sent_tokenize, word_tokenize
# sentence = "hi jons ,how are you ? are you doing some task. are you come."

# # print(sent_tokenize(sentence))
# print(word_tokenize(sentence))


############### Stemming  ########
# from nltk.stem import PorterStemmer
# stemmer = PorterStemmer()
# # print(stemmer.stem("playing"))
# print(stemmer.stem("plays"))
# print(stemmer.stem("played"))
# ## output play


########### Lemmatization  ############
# from nltk import WordNetLemmatizer
# lem = WordNetLemmatizer()
# print(lem.lemmatize("increases"))
# print(lem.lemmatize("running",pos='v'))


####### POS TAG #######
# from nltk import pos_tag,word_tokenize
# # from nltk.corpus import wordnet
# sentence = "hi jons ,how are you ? are you doing some task. are you come."

# tokens = word_tokenize(sentence)
# print(pos_tag(tokens))

############# Ngram ########
from nltk import ngrams
from nltk.tokenize import sent_tokenize, word_tokenize

sentence = " I love  to catch cricket"
n = 2
print(word_tokenize(sentence,n))

