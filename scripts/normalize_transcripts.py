import os
import re
import sys

def normalize_text(text):
    text = text.lower()
    text = text.replace("’", "'").replace("‘", "'")
    text = re.sub(r"[^a-z'\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

if __name__ == "__main__":
    folder = sys.argv[1]
    for fname in os.listdir(folder):
        if fname.endswith(".txt"):
            path = os.path.join(folder, fname)
            with open(path, encoding="utf8") as f:
                text = f.read()
            with open(path, "w", encoding="utf8") as f:
                f.write(normalize_text(text))

    print("All transcripts have been normalized.")