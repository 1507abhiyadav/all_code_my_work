from spacy import displacy
import spacy

# ##########   Modifying spaCy pipelines  ------>
# nlp = spacy.load('en_core_web_sm', exclude=['ner', 'parser'])
# # print(nlp.pipeline)

# ## Analyse the pipeline and store the analysis under 'pipe_analysis'
# pipe_analysis = nlp.analyze_pipes(pretty=True)
# # print(pipe_analysis)

# # #Examine the value stored under the key 'problems'
# print(pipe_analysis['problems'])


#########   Processing texts efficiently ----->

nlp = spacy.load('en_core_web_sm')
sents = ["On October 1, 2009, the Obama administration went ahead with a Bush administration program, increasing nuclear weapons production.", 
         "The 'Complex Modernization' initiative expanded two existing nuclear sites to produce new bomb parts.", 
         "The administration built new plutonium pits at the Los Alamos lab in New Mexico and expanded enriched uranium processing at the Y-12 facility in Oak Ridge, Tennessee."]
# # print(sents)
# # Feed the list of sentences to the pipe() method
# docs = nlp.pipe(sents)
# ## print(docs) #### output -->  <generator object Language.pipe at 0x000002784E1C9310>
# print(list(docs))  ## output ---> print  as list  without("" or '')


############  Adding custom attributes to spaCy objects  ---------------->
### Import the Doc object from the 'tokens' module in spaCy
from spacy.tokens import Doc

###### Add two custom attributes to the Doc object, 'age' and 'location'
###### using the set_extension() method.
Doc.set_extension("age", default=None)
Doc.set_extension("location", default=None)

#### Create a dictionary whose values consist of another dictionary
#### with three keys: 'age', 'location' and 'text'.
sents_dict = {0: {"age": 23, 
                  "location": "Helsinki", 
                  "text": "The Senate Square is by far the most important landmark in Helsinki."
                 },
              1: {"age": 35, 
                  "location": "Tallinn", 
                  "text": "The Old Town, for sure."
                 },
              2: {"age": 58, 
                  "location": "Stockholm", 
                  "text": "Södermalm is interesting!"
                 }
             }
docs = []
for key, data in sents_dict.items():
    # doc = nlp(data['text'])
    # doc._.age = data['age']
    # doc._.location = data['location']
    # docs.append(doc)
    # Retrieve the value under the key 'text' from the nested dictionary.
    # Feed this text to the language model under 'nlp' and assign the 
    # result to the variable 'doc'.
    doc = nlp(data['text'])
    
    # Retrieve the values for 'age' and 'location' from the nested dictionary.
    # Assign these values into the custom attributes defined for the Doc object.
    # Note that custom attributes reside under a pseudo attribute consisting of
    # an underscore '_'!  
    doc._.age = data['age']
    doc._.location = data['location']
    
    # Append the current Doc object under 'doc' to the list 'docs'
    docs.append(doc)

# for doc in docs:
    
#     # Print each Doc and the 'age' and 'location' attributes
#     print(doc, doc._.age, doc._.location)

# ###### Use a list comprehension to filter the Docs for those whose
# ###  'age' attribute has a value under 40.
# data = [doc for doc in docs if doc._.get('age') < 40]
# print(data)


########  Writing processed texts to disk    ######## ---------->
#### Import the DocBin object from the 'tokens' module in spacy
from spacy.tokens import DocBin
#### Initialize a DocBin object and add Docs from 'docs'
docbin = DocBin(docs=docs)
### print(docbin)
### Get the number of Docs in the DocBin
# print(docbin.__len__())
## Define and feed a string object the language model under 'nlp' and add the resulting Doc to the DocBin object 'docbin'
docbin.add(nlp("Yet another Doc object."))
### print(docbin)
### Verify that the Doc was added; length should be now 4
# print(docbin.__len__())
### Write the DocBin object to disk
docbin.to_disk(path='docbin.spacy')
### Initialise a new DocBin object and use the 'from_disk' method to load the data from the disk. Assign the result to the variable 'docbin_loaded'.
docbin_loaded = DocBin().from_disk(path='docbin.spacy')
# print(docbin_loaded)
docs_loaded = list(docbin_loaded.get_docs(nlp.vocab))
## Call the variable to examine the output
# print(docs_loaded)


##############     Simplifying output  ########### ------------------>
### ##  1:-     Merging noun phrases ##########--->
# for doc in docs:
#     # Loop over each noun chunk in the Doc object
#     for noun_chunk in doc.noun_chunks: 
#         ## Print noun chunk
#         print(noun_chunk)
##### Add component that merges noun phrases into single Tokens
# print(nlp.add_pipe('merge_noun_chunks'))
# nlp.pipeline
# docs = list(nlp.pipe(sents))
# # print(docs)
# # Loop over Tokens in the first Doc object in the list
# for token in docs[0]:
#     # Print out the Token and its part-of-speech tag
#     print(token, token.pos_)

######## 2:-      Merging named entities    ####### ---------->
# # Process the original sentences again
# docs = list(nlp.pipe(sents))
# # print(docs)
nlp.pipeline
nlp.add_pipe('merge_entities')
## Process the data again
docs = list(nlp.pipe(sents))
### Loop over Tokens in the third Doc object in the list
for token in docs[2]:
    # ###Print out the Token and its part-of-speech tag
    print(token, token.pos_)
