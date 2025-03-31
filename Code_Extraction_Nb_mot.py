from collections import Counter

def count_word_occurrences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    words = text.split()
    word_count = Counter(words)

    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    for word, count in sorted_word_count:
        print(f"'{word}': {count} fois")

file_path = "C:\\Users\\fou3d\\Downloads\\Exo-Note\\BOUDHAN_Ilies.txt"
count_word_occurrences(file_path)
