import spacy

# Loading the small English model from spaCy
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text: str) -> list:
    """
    Extract keywords from a given text. For the purpose of this function,
    keywords are considered as nouns and proper nouns.

    Parameters:
    - text (str): The text from which keywords are to be extracted.

    Returns:
    - list: A list containing extracted keywords.
    """
    # Using spaCy's NLP pipeline to process the given text
    doc = nlp(text)
    
    # Extracting nouns and proper nouns from the processed text as our keywords
    keywords = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
    
    return keywords
