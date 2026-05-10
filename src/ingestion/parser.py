from unstructured.partition.auto import partition

def partition_doc(file_path):

    elements = partition(
        filename=file_path,
        strategy="hi_res",
        infer_table_structure=True,
        extract_image_block_types=['Image'],
        extract_image_block_to_payload=True
    )

    return elements