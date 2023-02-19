def selection_sort(itemList):
    # take itemList len
    size = len(itemList)
    # outloop its itarate the size of array
    for i in range(size-1):
        minIndex = i
        # inside loop for compare each element
        for j in range(i+1, size):
            if itemList[j] < itemList[minIndex]:
                minIndex = j
        # if not match then swap
        if minIndex != i:
            temp = itemList[i]
            itemList[i] = itemList[minIndex]
            itemList[minIndex] = temp

    return itemList


itemList = [24, 1, 4, 99, 23]
print(selection_sort(itemList))
