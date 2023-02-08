import re
import sys
from deep_translator import GoogleTranslator

# Split the text into smaller groups up to 5000 characters without breaking lines so need to split on new lines
def split_text(text, max_len=4500):
    # Split the text into lines
    lines = text.split("\n")
    # List of chunks
    chunks = []
    # Chunk buffer
    chunk = ""

    # Loop through the lines
    for line in lines:
        # If the chunk is too long, add it to the list and reset the chunk
        if len(chunk + line) > max_len:
            chunks.append(chunk)
            chunk = ""
        # Add the line to the chunk
        chunk += line + "\n"

    # Add the last chunk to the list
    if chunk:
        chunks.append(chunk)

    # Return the list of chunks
    return chunks

def translate(text, source, target):
    # Split the text into smaller groups up to 5000 characters without breaking lines so need to split on new lines
    chunks = split_text(text)

    # Translate the text
    translated_text = ''
    for chunk in chunks:
        if source is None:
            source = 'auto'
        translated = GoogleTranslator(source=source, target=target).translate(text=chunk)
        translated_text += translated + "\n"

    # Remove extra new lines
    translated_text = re.sub(r'[\n]{3,}', '\n\n', translated_text.strip())
    translated_text = translated_text.strip()

    # Return the translated text
    return translated_text

if __name__ == "__main__":
    args = sys.argv

    # Handling the case when no file is passed
    if len(args) == 1:
        print("Please pass a file to translate")
        sys.exit(1)
    elif len(args) == 2:
        print("Please pass a target language")
        sys.exit(1)
    elif len(args) >= 3:
        text = str(open(args[1], encoding='utf8', newline='\n').read()).strip()

        # Handling `<filename> <target>`
        if len(args) == 3:
            translated = translate(text, None, args[2])
            print(translated)
        # Handling `<filename> <from> <target>`
        elif len(args) == 4:
            translated = translate(text, args[2], args[3])
            print(translated)

