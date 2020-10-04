from collections import defaultdict
from collections import Counter


def count_words_example_1(document: dict):
    """Подсчитываем кол-во слов в словаре"""

    word_counts = {}
    for word in document:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    common_count_words(document)


def count_words_example_2(document: dict):
    word_counts = {}
    for word in document:
        try:
            word_counts[word] += 1
        except KeyError:
            word_counts[word] = 1

    common_count_words(document)


def count_words_example_3(document: dict):
    word_counts = {}
    for word in document:
        previous_count = word_counts.get(word, 0)
        word_counts[word] = previous_count + 1

    common_count_words(document)


def common_count_words(document: dict):
    word_counts = defaultdict(int)
    for word in document:
        word_counts[word] += 1

    dd_list = defaultdict(list)
    dd_list[2].append(1)
    print(dd_list)

    dd_dict = defaultdict(dict)
    dd_dict["Joy"]["City"] = "Moscow"
    print(dd_dict)

    dd_pair = defaultdict(lambda: [0, 0])
    dd_pair[2][1] = 1
    print(dd_pair)

    c = Counter([0, 1, 2, 0])
    word_counts = c
    print(word_counts)


count_words_example_1({1: 2})
count_words_example_2({2: 3})
count_words_example_3({3: 4})