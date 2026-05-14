def build_retrieval_text(

    raw_text,

    keywords=None,

    figure_captions=None,

    table_summaries=None
):

    retrieval_text = ""


    # KEYWORDS

    if keywords:

        retrieval_text += (
            "=== KEYWORDS ===\n"

            + ", ".join(keywords)

            + "\n\n"
        )


    # TABLE SUMMARIES


    if table_summaries:

        retrieval_text += (
            "=== TABLE SUMMARIES ===\n"
        )

        for summary in table_summaries:

            retrieval_text += f"- {summary}\n"

        retrieval_text += "\n"


    # FIGURE CAPTIONS


    if figure_captions:

        retrieval_text += (
            "=== FIGURE INFORMATION ===\n"
        )

        for caption in figure_captions:

            retrieval_text += f"- {caption}\n"

        retrieval_text += "\n"

    # RAW CONTENT

    retrieval_text += (
        f"=== RAW CONTENT ===\n"
        f"{raw_text}"
    )


    return retrieval_text