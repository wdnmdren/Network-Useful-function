import os
import string
from collections import Counter

STOPWORDS = set()
STOPWORD_PATH = os.path.join(os.path.dirname(__file__), "data", "stopwords-en.txt")

if os.path.exists(STOPWORD_PATH):
    with open(STOPWORD_PATH, "r", encoding="utf-8") as f:
        for line in f:
            word = line.strip()
            if word:
                STOPWORDS.add(word.lower())
else:
    print(f"[Warning] Stopwords file not found at {STOPWORD_PATH}. Using empty stopword list.")

def get_word_frequencies_from_all_course_descriptions(course_descriptions):
    word_counter = Counter()
    for desc in course_descriptions:
        for word in desc.split():
            clean_word = word.strip(string.punctuation).lower()
            if not clean_word or clean_word in STOPWORDS:
                continue
            word_counter[clean_word] += 1
    return sorted(word_counter.items(), key=lambda item: item[1], reverse=True)
