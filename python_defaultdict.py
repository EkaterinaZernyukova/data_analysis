from collections import Counter


def most_common_count_words():
    word_counts = Counter({1: 2, 3: 1, 2: 3, 6: 8, 4: 12})
    print(word_counts)

    for word, count in word_counts.most_common(3):
        print(word, count)

    word_counts[99] = 18
    word_counts[106] = 344
    word_counts.update({123: 124, 2345: 1234})

    print(word_counts.most_common(3))


most_common_count_words()
