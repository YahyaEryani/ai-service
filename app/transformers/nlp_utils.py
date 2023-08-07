import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    doc = nlp(text)
    # For simplicity, let's consider nouns and proper nouns as our keywords
    keywords = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
    return keywords
