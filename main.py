from src.ingestion.parser import (
    partition_doc
)

from src.ingestion.chunking import (
    chunking_elements
)

from src.pipelines.processing_pipeline import (
    process_chunk
)

from src.retrieval.retrieval_testing import (
    test_retrieval
)

from src.retrieval.retriever import (
    create_retriever
)

from src.vectorstore.chroma_store import (
    create_vectorstore
)

# INPUT DOCUMENT

file_path = (
    "data/raw/attention_is_all_you_need.pdf"
)

# PARSE DOCUMENT


elements = partition_doc(
    file_path
)

# CHUNK DOCUMENT


chunks = chunking_elements(
    elements
)



# PROCESS CHUNKS


processed_docs = []


for idx, chunk in enumerate(chunks):

    doc = process_chunk(

        chunk=chunk,

        source=file_path,

        chunk_id=f"chunk_{idx}",

        page_no=chunk.metadata.page_number
    )


    if doc:

        processed_docs.append(
            doc
        )



print(
    f"Processed {len(processed_docs)} chunks"
)

# CREATE VECTORSTORE


vectorstore = create_vectorstore(
    processed_docs
)


# CREATE RETRIEVER


retriever = create_retriever(
    vectorstore
)

query = "What is the Transformer architecture?"

test_retrieval(
    retriever,
    query
)