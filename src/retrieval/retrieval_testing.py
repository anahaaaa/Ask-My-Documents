def test_retrieval(

    retriever,

    query
):

    docs = retriever.invoke(
        query
    )


    for i, doc in enumerate(docs):

        print(
            f"\n===== RESULT {i+1} =====\n"
        )

        print(
            doc.page_content[:1000]
        )

        print("\nMETADATA:\n")

        print(
            doc.metadata
        )