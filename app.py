import pytextrank
import spacy
import ssl
import os

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

os.system('python3 -m spacy download en_core_web_lg')

# nlp = spacy.load('en_core_web_lg')
