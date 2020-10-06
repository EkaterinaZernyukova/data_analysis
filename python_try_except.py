# def example_with_mistake(word_collection: list):
#     try:
#         sum(str(word_collection).isdigit) / 0
#     except ZeroDivisionError:
#         print("You can't")
#
#
# example_with_mistake([1, 2, 4, 6])

def example_with_mistake(x):
    try:
        x / 0
    except ZeroDivisionError:
        print("You can't")


example_with_mistake(66)
