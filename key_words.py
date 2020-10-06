def collection_words(key_words_for_collection: list):
    len(key_words_for_collection)
    if "boys" in key_words_for_collection:
        print("Ok")
    elif 235 in key_words_for_collection:
        print("mist")
    else:
        print("два первых условия не выполнены")

    copy_of_key_list = key_words_for_collection[2:4]
    if 234 in copy_of_key_list:
        print(copy_of_key_list)

    index = 0
    while (index < len(copy_of_key_list)):
        element = copy_of_key_list[index]

        if (str(element).isdigit() and element > 100):
            print(element, "больше 10")

        print(f"Index: {index}")
        index += 1


    # for copy_of_key in range(3):
    #     if copy_of_key == 1:
    #         continue
    #     if copy_of_key == 3:
    #         break
    #     print(copy_of_key)
    #
    # for key_words_for_collection in range(6):
    #     print("довольно")


collection_words(["boy", "summer", 234, "\t"])
