from keybert import KeyBERT
from utils.config import KEYWORD_TOP_N


kw_model = KeyBERT()


def extract_keywords(text, top_n=KEYWORD_TOP_N):

    keywords = kw_model.extract_keywords(
        
        text,
        keyphrase_ngram_range=(1,3),
        stop_words='english',
        top_n=top_n
        
    )

    keyword_list = [keyword[0] for keyword in keywords]

    return keyword_list