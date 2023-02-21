# initial array
def make_array():
    arr = []
    return arr

# Add item on array


def add(arr, item):
    arr.append(item)

# Remove item from array


def delete(arr, item):
    if len(arr) > 0:
        arr.remove(item)
    else:
        print('Array is empty')

# Search item on array


def linerSearch(arr, item):
    # Base case
    if len(arr) < 0:
        return False

    # Iterate until match item

    for i in range(0, len(arr)):
        if (arr[i] == item):
            return i

    return "Item Not Found"


# initial array
d_array = make_array()
add(d_array, 3)
add(d_array, 4)
add(d_array, 6)
add(d_array, 8)
add(d_array, 10)
add(d_array, 5)

print("Array is: " + str(d_array))

item = 10

search_result = linerSearch(d_array, item)

print("Element is present at index: " + str(search_result))
