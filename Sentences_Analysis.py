sentence = input("Enter a sentences: ")
words = sentence.lower().split()
clean_sentence = " ".join(words)

total_words = len(words)
python_count = words.count("python")

if total_words > 0:
    longest_word = max(words, key=len)
else:
    longest_word = "No words entered"

print("Cleaned sentences: ", clean_sentence)
print("total words: ", total_words)
print("Times 'python' appears: ", python_count)
print("Longest words: ", longest_word)
