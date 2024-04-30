import re
# Import pos tagger
from nltk import pos_tag


def preprocess_text(text):
    # Lowercase the text
    text = text.lower()
    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Remove extra whitespaces
    text = re.sub(r'\s+', ' ', text).strip()
    # Do POS tagging to find items and their attributes
    text = pos_tag(text.split())
    # Only keep nouns and adjectives
    text = [word for word, tag in text if tag in ['NN', 'NNS', 'JJ']]
    # Join the words back into a single string
    text = ' '.join(text)
    return text