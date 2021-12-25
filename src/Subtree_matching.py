# two drawbacks in rule based matching

#We have to be extremely creative to come up with new rules to capture different patterns
# It is difficult to build patterns that generalize well across different sentences
import re
import string
import nltk
import spacy
import pandas as pd
import numpy as np
import math
from tqdm import tqdm

from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy import displacy

pd.set_option('display.max_colwidth', 200)

# Loading a spacy model

nlp = spacy.load("en_core_web_sm")

text = "Tableau was recently acquired by Salesforce." 
doc = nlp(text) 
# displacy.render(doc, style='dep',jupyter=True)

# X acquired Y relationships
text = "Tableau was recently acquired by Salesforce"
doc = nlp(text)

# for tok in doc:
#     print(tok.text,"-->",tok.dep_,"-->",tok.pos_)

def subtree_matcher(doc): 
  x = '' 
  y = '' 
  
  for i, tok in enumerate(doc): 
    if tok.dep_.find("subjpass") == True: 
      y = tok.text 

    if tok.dep_.endswith("obj") == True: 
      x = tok.text 
      
  return x,y

print(subtree_matcher(doc))


text_2 = "Careem, a ride hailing major in middle east, was acquired by Uber." 

doc_2 = nlp(text_2) 
print(subtree_matcher(doc_2))

text_3 = "Salesforce recently acquired Tableau." 
doc_3 = nlp(text_3) 
print(subtree_matcher(doc_3))

# for tok in doc_3:    
#   print(tok.text, "-->",tok.dep_, "-->",tok.pos_)

# Modifying function to adjust active voice too

def new_subtree_matcher(doc):
  subjpass = 0

  for i,tok in enumerate(doc):
    # find dependency tag that contains the text "subjpass"    
    if tok.dep_.find("subjpass") == True:
      subjpass = 1

  x = ''
  y = ''

  # if subjpass == 1 then sentence is passive
  if subjpass == 1:
    for i,tok in enumerate(doc):
      if tok.dep_.find("subjpass") == True:
        y = tok.text

      if tok.dep_.endswith("obj") == True:
        x = tok.text
  
  # if subjpass == 0 then sentence is not passive
  else:
    for i,tok in enumerate(doc):
      if tok.dep_.endswith("subj") == True:
        x = tok.text

      if tok.dep_.endswith("obj") == True:
        y = tok.text

  return x,y

print(new_subtree_matcher(doc_3))
print(new_subtree_matcher(nlp("Tableau was recently acquired by Salesforce.")))