#!/usr/bin/env python
# coding: utf-8

# In[11]:


import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import random
import re



# In[12]:


sentence = "The quick brown fox jumps over the lazy dog."
word = "quick"
print("Original Sentence:", sentence)


# In[13]:


tokens=nltk.word_tokenize(sentence)


# In[14]:


for synset in wordnet.synsets(word):
    for synonym in synset.lemmas():
        synonyms.append(synonym.name())


# In[15]:


new_sentence = ""
for i in tokens:
    if word == i:
        new_sentence += random.choice(synonyms) + " "
    else:
        new_sentence += i + " "


# In[16]:


print("New Sentence:", new_sentence.strip())


# In[17]:


text = "This is a sample text with some words to be replaced. Another line with words."
regex = r"\b(sample)\b"
replacement = "hello"
new_text = re.sub(regex, replacement, text)


# In[18]:


print(new_text)


# In[19]:


print("Original text:", text)
print("Modified text:", new_text)


# In[ ]:




