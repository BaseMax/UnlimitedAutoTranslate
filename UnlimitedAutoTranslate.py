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

args = sys.argv

# Handling the case when no file is passed
if len(args) == 1:
    print("Please pass a file to translate")
    sys.exit(1)
elif len(args) == 2:
    print("Please pass a target language")
    sys.exit(1)
elif len(args) > 3:
    text = str(open(args[1], encoding='utf8', newline='\n').read()).strip()

    # Handling `<filename> <target>`
    if len(args) == 3:
        translated = translate(text, None, args[2])
        print(translated)
    # Handling `<filename> <from> <target>`
    elif len(args) == 4:
        translated = translate(text, args[2], args[3])
        print(translated)

