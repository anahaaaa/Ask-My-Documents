from langchain_core.documents import Document

from src.ingestion.content_extraction import (
    extract_content
)

from src.enrichment.figure_captioning import (
    generate_figure_caption
)

from src.enrichment.table_summary import (
    summarize_table
)

from src.enrichment.keywords import (
    extract_keywords
)

from src.enrichment.metadata import (
    build_metadata
)

from src.enrichment.retrieval_text import (
    build_retrieval_text
)

def process_chunk(

    chunk,

    source: str,

    chunk_id: str,

    page_no: int
) -> Document:
    

    # Separate content types

    chunk_content_data = extract_content(
        chunk
    )

    raw_text = chunk_content_data["text"]

    tables = chunk_content_data["tables"]

    images = chunk_content_data["images"]


    # Generate figure captions

    figure_captions = []

    if images:

        for image_base64 in images:

            try:

                caption = generate_figure_caption(
                    image_base64
                )

                if caption:

                    figure_captions.append(
                        caption
                    )

            except Exception as e:

                print(
                    f"Figure caption failed: {e}"
                )


    # STEP 3: Generate table summaries

    table_summaries = []

    if tables:

        for table_html in tables:

            try:

                summary = summarize_table(
                    table_html
                )

                if summary:
                    
                    table_summaries.append(
                        summary
                    )

            except Exception as e:

                print(
                    f"Table summary failed: {e}"
                )

    # STEP 4: Extract keywords

    try:

        keywords = extract_keywords(
            raw_text
        )

    except Exception as e:

        print(
            f"Keyword extraction failed: {e}"
        )

        keywords = []


    # Build metadata

    metadata = build_metadata(

        source=source,

        page_no=page_no,

        chunk_id=chunk_id,

        figure_captions=figure_captions,

        table_summary=table_summaries,

        keywords=keywords,

        chunk_content_data=chunk_content_data
    )



    # Build retrieval text

    retrieval_text = build_retrieval_text(

        raw_text=raw_text,

        keywords=keywords,

        figure_captions=figure_captions,

        table_summaries=table_summaries
    )


    
    # Create final document


    final_doc = Document(

        page_content=retrieval_text,

        metadata=metadata
    )


    return final_doc