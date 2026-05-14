from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from src.utils.config import (
    EMBEDDING_MODEL_NAME
)


# EMBEDDING MODEL

embedding_model = HuggingFaceEmbeddings(

    model_name=EMBEDDING_MODEL_NAME,

    encode_kwargs={
        "normalize_embeddings": True
    }
)