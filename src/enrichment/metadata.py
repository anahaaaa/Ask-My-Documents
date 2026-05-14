def build_metadata(
    source,
    page_no,
    chunk_id,
    figure_captions,
    table_summary,
    keywords,
    chunk_content_data
):

    metadata = {
    
        "source": source,
    
        "page": page_no,
    
        "chunk_id": chunk_id,
    
        "chunk_length": len(
            chunk_content_data["text"]
        ),
    
        "has_table": len(
            chunk_content_data["tables"]
        ) > 0,
    
        "has_image": len(
            chunk_content_data["images"]
        ) > 0,
    
        "has_keywords": len(
            keywords
        ) > 0,
    
        "content_types": " | ".join(
            chunk_content_data["types"]
        ),
    
        "num_tables": len(
            chunk_content_data["tables"]
        ),
    
        "num_images": len(
            chunk_content_data["images"]
        ),
    
        "figure_captions": " | ".join(
            figure_captions
        ),
    
        "keywords": " | ".join(
            keywords
        ),
    
        "table_summaries": " | ".join(
            table_summary
        )
    }