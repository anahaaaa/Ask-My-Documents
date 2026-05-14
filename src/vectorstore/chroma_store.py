from langchain_chroma import Chroma

from src.utils.config import (
    CHROMA_DB_PATH
)



def create_vectorstore(

    processed_docs,

    embedding_model
):

    vectorstore = Chroma.from_documents(

        documents=processed_docs,

        embedding=embedding_model,

        persist_directory=CHROMA_DB_PATH
    )

    return vectorstore