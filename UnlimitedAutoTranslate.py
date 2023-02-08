import sys
from deep_translator import GoogleTranslator

# Split the text into smaller groups up to 5000 characters without breaking lines so need to split on new lines
def split_text(text, max_len=4500):
    chunks = []
    lines = text.split("\n")
    chunk = ""
    for line in lines:
        if len(chunk + line) > max_len:
            chunks.append(chunk)
            chunk = ""
        chunk += line + "\n"
    if chunk:
        chunks.append(chunk)
    return chunks

