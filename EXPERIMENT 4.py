#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
nltk.download('punkt')  # For tokenization
nltk.download('stopwords')  # For stop word removal
nltk.download('wordnet')  # For lemmatization
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import PorterStemmer, WordNetLemmatizer
import random
import re

text = "This is a sample text to demonstrate text preprocessing techniques."
tokens = word_tokenize(text)
print(tokens)

stop_words = set(stopwords.words('english'))
stop_removed = [word for word in tokens if word.lower() not in stop_words]
print(stop_removed)

custom_stop = ["text", "sample"]
stop_words.update(custom_stop)
stop_removed_new = [word for word in tokens if word.lower() not in stop_words]
print(stop_removed_new)

stemmer = PorterStemmer()
stem_removed = [stemmer.stem(word) for word in stop_removed]
print(stem_removed)

lemmatizer = WordNetLemmatizer()
pos_tags = nltk.pos_tag(tokens)
lemmatized_words = []
for word, pos_tag in pos_tags:
    if pos_tag.startswith('V'):
        pos = 'v'
    elif pos_tag.startswith('N'):
        pos = 'n'
    elif pos_tag.startswith('J'):
        pos = 'a'
    elif pos_tag.startswith('R'):
        pos = 'r'
    else:
        pos = 'n'
    lemmatized_words.append(lemmatizer.lemmatize(word, pos=pos))
print(' '.join(lemmatized_words))

def replace_with_synonyms(sentence, target_word):
    synonyms = []
    for synset in wordnet.synsets(target_word):
        for synonym in synset.lemmas():
            synonyms.append(synonym.name())
    if synonyms:
        chosen_synonym = random.choice(synonyms)
        return sentence.replace(target_word, chosen_synonym)
    return sentence

sentence = "The quick brown fox jumps over the lazy dog."
word_to_replace = "quick"
new_sentence = replace_with_synonyms(sentence, word_to_replace)
print(sentence)
print(new_sentence)

text = "This is a sample text with some words to be replaced. Another line with words."
regex = r"\b(sample)\b"
replacement = "hello"
new_text = re.sub(regex, replacement, text)
print(text)
print(new_text)


# In[ ]:




