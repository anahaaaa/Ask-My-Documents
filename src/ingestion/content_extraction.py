from typing import Dict, Any

def extract_content(chunk) -> Dict[str, Any]:

    chunk_content_data = {
        'text' : chunk.text,
        'tables' : [],
        'images' : [],
        'types' : set(['text'])
    }


    if hasattr(chunk, 'metadata') and hasattr(chunk.metadata, 'orig_elements'):
         for element in chunk.metadata.orig_elements:

            if element.category == 'Table':

                 chunk_content_data['types'].add('table')
                 table_html = getattr(element.metadata, 'text_as_html', element.text)
                 chunk_content_data['tables'].append(table_html)

            
            elif element.category == 'Image':

                image_base64 = getattr(
                    element.metadata,
                    'image_base64',
                    None
                )

                if image_base64:

                    chunk_content_data['types'].add('image')

                    chunk_content_data['images'].append(
                        image_base64
                    )

    chunk_content_data['types'] = list(chunk_content_data['types'])

    return chunk_content_data