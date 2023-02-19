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

# Recursion  method


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

# Divide and conqure method
# Iterative method


def iterative_binary_serach(arr, item):
    # base case
    if len(arr) < 0:
        return False

    # Sorting if arr is unsorted
    arr.sort()
    head = 0
    tail = len(arr)-1
    mid = 0

    while head <= tail:
        mid = (head+tail)//2

        # if mid is greater then item then igonre the right site of array
        if arr[mid] > item:
            tail = mid-1
        # If mid element is smaller then item then ignore left site of array
        elif arr[mid] < item:
            head = mid+1
        # Mid is equal to item then return mid
        else:
            return mid

    return "No Item Found"


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

item = 10
item2 = 6

search_result = binarySearch(d_array, 0, len(d_array)-1, item)

iterative_binary_result = iterative_binary_serach(d_array, item2)

print("Element is present at index: " + str(search_result))
print("Iterative search result at index: " + str(iterative_binary_result))
