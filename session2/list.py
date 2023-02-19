# fuel_level : [287, 290, 250, 100, "200", 120, 200, "null", -99, null]
# list of data
from asyncio.windows_events import NULL

# fuel_level = [287, 290, 250, 100, "200", 120, 200, "null", -99, NULL]
# fuel_level2 = [287, 290, 250, 100]

# print(fuel_level[-2])  # Access list item by index
# fuel_level.append(12)  # Add new item in list
# print(fuel_level)
# fuel_level.extend(fuel_level2)  # extend
# del (fuel_level[1])
# print(fuel_level)
# print(fuel_level[4:8])  # print range wise

# # Count
# # check the count of 2
# numbers = [2, 3, 5, 2, 11, 2, 7]
# # check the count of 2
# count = fuel_level2.count(3)
# print('Count of 2:', count)

# # pop
# # create a list of prime numbers
# prime_numbers = [2, 3, 5, 7]

# # reverse the order of list elements
# prime_numbers.reverse()
# # remove the element at index 2
# removed_element = prime_numbers.pop(1)  # pop
# prime_numbers.sort()  # sort
# print('Removed Element:', removed_element)

# # remove all elements
# # prime_numbers.clear()

# print('Updated List:', prime_numbers)

# # print using foreach
# for level in fuel_level:
#     print(level)

a = []
b = [2, 10, 11, 3]


def new_func(a, b):
    a.extend(b)
    a.sort()


new_func(a, b)
print(a)
