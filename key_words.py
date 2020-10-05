def collection_words():
    key_words_for_collection = ["boy", "summer", 234, "\t"]
    len(key_words_for_collection)
    if "boys" in key_words_for_collection:
        print("Ok")
    elif 235 in key_words_for_collection:
        print("mist")
    else:
        print("два первых условия не выполнены")

    copy_of_key = key_words_for_collection[2:3]
    print(copy_of_key)

    for copy_of_key in range(3):
        if copy_of_key == 1:
            continue
        if copy_of_key == 3:
            break
        print(copy_of_key)

    for key_words_for_collection in range(6):
        print("довольно")


collection_words()
