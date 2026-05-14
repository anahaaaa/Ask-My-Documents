from src.utils.config import (
    TOP_K_RETRIEVAL
)



def create_retriever(
    vectorstore
):

    retriever = vectorstore.as_retriever(

        search_kwargs={
            "k": TOP_K_RETRIEVAL
        }
    )

    return retriever