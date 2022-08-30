import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
text = "The Federal Bureau of Investigation has been ordered to track down as many as 3,000 Iraqis in this country whose visas have expired, the Justice Department said yesterday."
doc = nlp(text)
# print(doc)
###### token in spacy library
# for token in  doc:
    # print(token):

###### part of speech (POS) tag ---->
# for token in  doc:
    # print(token, token.pos_ ,token.tag_)

### morphemes---->>
# for token in  doc:
#     print(token, token.morph)
###   print(doc[22].morph.get('Aspect'))   ### output ---->  ['Perf']
####  print(doc[21].morph.to_dict())      ### output ---->{'Mood': 'Ind', 'Tense': 'Pres', 'VerbForm': 'Fin'}

## ## Syntactic parsing or (dependency parsing ) ---->
# for token in doc:
#     print(token,token.dep_)

## for token in doc:
#   # ### # Print the index of current token, the token itself, the dependency, the head and its index
##     print(token.i, token, token.dep_, token.head.i, token.head)

######## displacy ####
# text = "When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously."

# nlp = spacy.load("en_core_web_sm")
# doc = nlp(text)
# displacy.serve(doc, style="ent",options={'compact': True})

#### print(spacy.explain('det')) ## output ---> determiner
#### print(spacy.explain('pobj')) ## output ---> object of preposition

######### Sentence segmentation--->
# for number,sent in enumerate(doc.sents):
#      ### Print the token and its dependency tag
#     print(number, sent)

######## Lemmatization ----->>
# for token in doc:
#     print(token,token.lemma_)

#######  Named entity recognition (NER)  -->

# print(doc.ents)  #### output --(The Federal Bureau of Investigation, as many as 3,000, Iraqis, the Justice Department, yesterday)
# print(type(doc.ents[0]))  ### output  --->. <class 'spacy.tokens.span.Span'>
# ##Loop over the named entities in the Doc object 
# for ent in doc.ents:

#     ### Print the named entity and its label   ---->>  .label_ of each Span object.
#     print(ent.text, ent.label_)

# #####Print the named entity and indices of its start and end Tokens
# print(doc.ents[0], doc.ents[0].start, doc.ents[0].end)

### Loop over a slice of the Doc object that covers the first named entity
# for token in doc[doc.ents[0].start: doc.ents[0].end]:
    
#     #### Print the Token and its index
#     print(token, token.i)
