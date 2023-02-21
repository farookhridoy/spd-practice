
def merge(arr,left,mid,right):
    left_size = mid-left+1
    right_size = right-mid

    #Create temp arrays
    left_arr = [0] * (left_size)
    right_arr = [0] * (right_size)
    #Copy data to temp arrays
    for i in range(0, left_size):
        left_arr[i] = arr[left+i]
    
    for j in range(0,right_size):
        right_arr[j] = arr[mid+1+j]
    
    # Initial index of arrays and merge subarray index
    i=j=0 
    k=left
    while i < left_size and j < right_size:
        if left_arr[i]<=right_arr[j]:
            arr[k]=left_arr[i]
            i+=1
        else:
            arr[k] = right_arr[j]
            j+=1
        k+=1
    # If any remaing element left on the left sub array then put it in main array
    while i <left_size:
        arr[k] = left_arr[i]
        i+=1
        k+=1
    # If any remaing element rifht on the left sub array then put it in main array
    while j < right_size:
        arr[k] = right_arr[j]
        j+=1
        k+=1

#Make a function for merge sort
def merge_sort(arr, l,r):
    #Base case: If the length of the array is less then 1 then the array is already sorted
    if l>=r:
        return False
    #Find mid of the array if the array is pass the base case
    mid = l+(r-l)//2

    #Sort the left and right subarray after divide by mid
    #Call two recursive function for both left and right array
    merge_sort(arr,l,mid)
    merge_sort(arr,mid+1,r)
    merge(arr,l,mid,r)


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
#array length
arr_length = len(arr)
#print given array
print("Given array is: "+str(arr))

#call the sorting algorithm
merge_sort(arr,0,arr_length-1)

print("\n\nSorted array is: "+str(arr))
