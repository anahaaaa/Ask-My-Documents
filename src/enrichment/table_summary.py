import re
import torch
from bs4 import BeautifulSoup

from transformers import (
    AutoTokenizer,
    Qwen2VLForConditionalGeneration
)

from src.utils.config import (
    VISION_MODEL_NAME,
    MAX_NEW_TOKENS
)


# LOAD MODEL + TOKENIZER


tokenizer = AutoTokenizer.from_pretrained(
    VISION_MODEL_NAME
)

model = Qwen2VLForConditionalGeneration.from_pretrained(

    VISION_MODEL_NAME,

    torch_dtype=torch.float16,

    device_map="auto"
)

# clean html

def clean_tablehtml(table_html):

    soup = BeautifulSoup(table_html, "html.parser")
    text = soup.get_text(separator=" ")

    return text


# BUILD TABLE PROMPT


def build_table_prompt(
    text
):

    prompt = f"""

You are analyzing a table extracted from a document.

TABLE CONTENT:
{text}

TASK:
Generate a concise but information-rich summary
for this table.

Include:
- what the table contains or compares
- important metrics or values
- trends or observations
- key entities/categories
- notable insights

Optimize the summary for semantic retrieval
in a RAG system.

TABLE SUMMARY:

"""

    return prompt



# =====================================
# TABLE SUMMARIZATION
# =====================================

def summarize_table(
    table_html
):

    table_text = clean_table_html(
        table_html
    )


    prompt = build_table_prompt(
        table_text
    )


    inputs = tokenizer(

        prompt,

        return_tensors="pt",

        truncation=True,

        max_length=2048

    ).to(model.device)


    generated_ids = model.generate(

        **inputs,

        max_new_tokens=MAX_NEW_TOKENS
    )


    output = tokenizer.decode(

        generated_ids[0],

        skip_special_tokens=True
    )


    return output