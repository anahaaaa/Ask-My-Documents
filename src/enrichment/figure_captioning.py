from PIL import Image

import base64
import io
import torch

from transformers import (
    Qwen2VLForConditionalGeneration,
    AutoProcessor
)

from src.utils.config import (
    VISION_MODEL_NAME,
    MAX_NEW_TOKENS
)


# LOAD MODEL


model = Qwen2VLForConditionalGeneration.from_pretrained(

    VISION_MODEL_NAME,

    torch_dtype=torch.float16,

    device_map="auto"
)

processor = AutoProcessor.from_pretrained(
    VISION_MODEL_NAME
)


# BASE64 → PIL


def base64_to_pil(
    base64_string
):

    image_data = base64.b64decode(
        base64_string
    )

    image = Image.open(

        io.BytesIO(image_data)

    ).convert("RGB")


    image.thumbnail((1024, 1024))

    return image


# FIGURE CAPTION GENERATION


def generate_figure_caption(
    image_base64
):

    try:

        pil_image = base64_to_pil(
            image_base64
        )


        messages = [

            {
                "role": "user",

                "content": [

                    {
                        "type": "image",
                        "image": pil_image
                    },

                    {
                        "type": "text",

                        "text":
                        """
                        Generate a concise retrieval-oriented
                        caption for this document image.

                        Focus on:
                        - diagrams
                        - figures
                        - architectures
                        - charts
                        - workflows
                        - technical concepts

                        Keep the caption concise but
                        semantically informative.
                        """
                    }
                ]
            }
        ]


        text_prompt = processor.apply_chat_template(

            messages,

            tokenize=False,

            add_generation_prompt=True
        )


        inputs = processor(

            text=[text_prompt],

            images=[pil_image],

            return_tensors="pt"

        ).to(model.device)


        generated_ids = model.generate(

            **inputs,

            max_new_tokens=MAX_NEW_TOKENS
        )


        generated_text = generated_ids[
            0,
            inputs.input_ids.shape[1]:
        ]


        caption = processor.decode(

            generated_text,

            skip_special_tokens=True
        )


        return caption.strip()


    except Exception as e:

        print(
            f"Caption generation failed: {e}"
        )

        return ""