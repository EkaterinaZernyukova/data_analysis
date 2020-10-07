def example_with_mistake(num_collection: list):
    try:
        sum(num_collection) / 0
        # sum(str(num_collection).isdigit) / 0
    except ZeroDivisionError as error:
        print(f"You can't. {error}")



example_with_mistake([1, 2, 4, 6])

# def example_with_mistake(x):
#     try:
#         x / 0
#     except ZeroDivisionError:
#         print("You can't")
#
#
# example_with_mistake(66)
