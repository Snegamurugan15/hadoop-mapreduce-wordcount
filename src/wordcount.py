from collections import Counter
import re, sys
STOPWORDS = {"the", "and", "of", "to", "in", "a", "is", "for", "on", "with"}
def count_words(text):
    words = re.findall(r"[A-Za-z']+", text.lower())
    return Counter(w for w in words if w not in STOPWORDS)
if __name__ == "__main__":
    text = sys.stdin.read()
    for word, count in count_words(text).most_common():
        print(f"{word}	{count}")
