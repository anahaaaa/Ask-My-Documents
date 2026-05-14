from unstructured.chunking.title import chunk_by_title
from utils.config import MAX_CHARACTERS, NEW_AFTER_N_CHARS, COMBINE_TEXT_UNDER_N_CHARS

def chunking_elements(elements):

    chunks = chunk_by_title(
        elements,
        max_characters = MAX_CHARACTERS,
        new_after_n_chars = NEW_AFTER_N_CHARS,
        combine_text_under_n_chars=COMBINE_TEXT_UNDER_N_CHARS
    )

    return chunks