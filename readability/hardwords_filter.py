# Most common words
common_words = set()
with open('20k.txt', 'r') as f:
    for word in f.readlines():
        common_words.add(word.strip())
# Hardwords from https://en.wikipedia.org/wiki/List_of_medical_roots,_suffixes_and_prefixes
hardwords = set()
with open('hardwords.txt', 'r') as f:
    for word in f.readlines():
        word = word.lower()
        if word.strip() not in common_words:
            hardwords.add(word.strip())
with open('hardwords_filtered.txt', 'w') as f:
    f.write("\n".join(hardwords))