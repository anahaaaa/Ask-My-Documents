from unstructured.partition.auto import partition
from utils.config import PDF_PARTITION_STRATEGY

def partition_doc(file_path):

    elements = partition(
        filename=file_path,
        strategy=PDF_PARTITION_STRATEGY,
        infer_table_structure=True,
        extract_image_block_types=['Image'],
        extract_image_block_to_payload=True
    )

    return elements