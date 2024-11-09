
text: str =input('Enter the text : ')
word_counts:dict[str,int] = {}
for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1
unique_words = set(word_counts.keys())
print("Word counts:", word_counts)
print("Unique words:", unique_words)
