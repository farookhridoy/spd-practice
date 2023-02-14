
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


def binarySearch(arr, low, high, item):
    # Base case
    if len(arr) < 0:
        return False
    # Binary search works on sorted array. if not sorted then sort the array.
    arr.sort()
    # Divide and conqure
    if high >= low:
        mid = low+(high-low)//2
        # If foudn in mid then return mid index
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return binarySearch(arr, low, mid-1, item)
        else:
            return binarySearch(arr, mid+1, high, item)
    else:
        return "Not found"


# initial array
d_array = make_array()
add(d_array, 3)
add(d_array, 4)
add(d_array, 6)
add(d_array, 8)
add(d_array, 10)
add(d_array, 5)

d_array.sort()
print("Array is: " + str(d_array))

item = 5

search_result = binarySearch(d_array, 0, len(d_array)-1, item)

print("Element is present at index: " + str(search_result))
