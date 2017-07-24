# Finds the synonyms for each term in the openFDA Library
# Populates Taxonomy with similar words aka more comprehensive

from PyDictionary import PyDictionary
from bs4 import BeautifulSoup

dictionary = PyDictionary()
products = ["ENBREL"]
events = ['PAIN', 'INEFFECTIVE']

synonyms = []
for drug in products:
  for term in events:
    # Dictionary only allows synonyms for single words
    if len(term.split()) == 1:
      synonyms.append(dictionary.synonym(term))
    # If adverse event is multiple words, skip to next event
    else:
      pass

print(synonyms)
