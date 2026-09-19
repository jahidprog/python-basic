# Mini Project: Word Counter

def word_counter(text):
    words = text.lower().split()

    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


text = input("Paste some text: ")

result = word_counter(text)

print("\nWord frequency:")
for word, count in sorted(result.items(), key=lambda item: item[1], reverse=True):
    print(f"{word}: {count}")
