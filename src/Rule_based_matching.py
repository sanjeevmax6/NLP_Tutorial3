#Information Extraction - extracting triples

# 3 types
# Rule based approach3
# Supervised
# Semi-supervised

# example
# Agar is a substance prepard from a mixture of red algae, such as Geldium, for laboratory or industrial use
# Here "red algae" is Hypernym and Geldium is "Hyponym"
# Since we can infer that "Geldium" is a type of "red algae" by just looking at the structue of sentence

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

# Sample
# text = "GDP in developing countries such as Vietnam will continue growing at a high rate."

# doc = nlp(text)

# extracting syntactic structure of the sentence

# for tok in doc:
    # print(tok.text, "-->", tok.dep_, "-->", tok.pos)

# pattern = [{'POS':'NOUN'}, 
#            {'LOWER': 'such'}, 
#            {'LOWER': 'as'}, 
#            {'POS': 'PROPN'}]

# Extracting pattern
# matcher = Matcher(nlp.vocab)
# matcher.add("matching_1", [pattern])

# matches = matcher(doc)
# span = doc[matches[0][1]:matches[0][2]]

# print(span.text)

# Tuning the algorithm to capture "developing countries" instead of just "countries"

# matcher = Matcher(nlp.vocab)

# Defining pattern

# pattern = [{'DEP':'amod', 'OP':"?"}, 
#            {'POS':'NOUN'},
#            {'LOWER': 'such'},
#            {'LOWER': 'as'},
#            {'POS': 'PROPN'}]

# matcher.add("matching_1", [pattern])
# matches = matcher(doc)

# span = doc[matches[0][1]: matches[0][2]]
# print(span.text)

# Using Hearst patterns to extract hypernyms and hyponyms

# doc = nlp("Here is how you can keep your car and other vehicles clean.") 

# for tok in doc:
#     print(tok.text, "-->",tok.dep_, "-->",tok.pos_)

#Defining matching for this

# matcher = Matcher(nlp.vocab)

# pattern = [{'DEP':'amod', 'OP':"?"}, 
#            {'POS':'NOUN'}, 
#            {'LOWER': 'and', 'OP':"?"}, 
#            {'LOWER': 'or', 'OP':"?"}, 
#            {'LOWER': 'other'}, 
#            {'POS': 'NOUN'}] 

# matcher.add("matching_1", [pattern])

# matches = matcher(doc) 
# print(len(matches))
# span = doc[matches[0][1]: matches[0][2]] 
# print(span.text)

# matcher = Matcher(nlp.vocab) 

#define the pattern 
# pattern = [{'DEP':'amod', 'OP':"?"}, 
#            {'POS':'NOUN'}, 
#            {'LOWER': 'and', 'OP':"?"}, 
#            {'LOWER': 'or', 'OP':"?"}, 
#            {'LOWER': 'other'}, 
#            {'POS': 'NOUN'}] 
           
# matcher.add("matching_1", [pattern]) 

# matches = matcher(doc) 
# span = doc[matches[0][1]:matches[0][2]] 
# print(span.text)

doc = nlp("Eight people, including two children, were injured in the explosion") 

# for tok in doc: 
#   print(tok.text, "-->",tok.dep_, "-->",tok.pos_)

# matcher = Matcher(nlp.vocab) 

# #define the pattern 
# pattern = [{'DEP':'nummod','OP':"?"}, # numeric modifier 
#            {'DEP':'amod','OP':"?"}, # adjectival modifier 
#            {'POS':'NOUN'}, 
#            {'IS_PUNCT': True}, 
#            {'LOWER': 'including'}, 
#            {'DEP':'nummod','OP':"?"}, 
#            {'DEP':'amod','OP':"?"}, 
#            {'POS':'NOUN'}] 
                               
# matcher.add("matching_1", [pattern]) 

# matches = matcher(doc) 
# span = doc[matches[0][1]:matches[0][2]] 
# print(span.text)

doc = nlp("A healthy eating pattern includes fruits, especially whole fruits.") 

# for tok in doc: 
#   print(tok.text, tok.dep_, tok.pos_)


# Matcher class object 
matcher = Matcher(nlp.vocab)

#define the pattern 
pattern = [{'DEP':'nummod','OP':"?"}, 
           {'DEP':'amod','OP':"?"}, 
           {'POS':'NOUN'}, 
           {'IS_PUNCT':True}, 
           {'LOWER': 'especially'}, 
           {'DEP':'nummod','OP':"?"}, 
           {'DEP':'amod','OP':"?"}, 
           {'POS':'NOUN'}] 
           
matcher.add("matching_1", [pattern]) 

matches = matcher(doc) 
span = doc[matches[0][1]:matches[0][2]] 
print(span.text)