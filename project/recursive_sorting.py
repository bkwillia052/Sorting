### helper function
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a = 0
    b = 0
    print("mergeL:", arrA, "mergeR:", arrB)
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range( 0, elements ):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


### recursive sorting function
def merge_sort( arr ):
    print("array:",arr, "Len:",len(arr))
    
    if len( arr ) > 1:
        left = merge_sort( arr[ 0 : int(len(arr)/2) ] )
        print("L:", left)
        right = merge_sort( arr[ int(len(arr)/2) : ] )
        print("R:", right)
        arr = merge( left, right )   # merge() defined later
    
    print("outside of if:", arr)
    return arr

arr = [5, 4, 3, 5, 7, 9, 20, 12, 34, 57]

#print(merge_sort(arr))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION
def quick_sort( arr, low, high ):
    # base 
    if high-low <= 0:
        return arr

    
    pivot = low
    for i in range(low+1, high+1):
        if arr[i] < arr[pivot]:
            arr[i], arr[pivot+1] = arr[pivot+1], arr[i]

            arr[pivot], arr[pivot+1] = arr[pivot+1], arr[pivot]
        
            pivot += 1
    
    
    arr = quick_sort(arr, low, pivot-1) #Left
    arr = quick_sort(arr, pivot+1, high) #Right

    return arr
    
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(quick_sort(arr1, 0, len(arr1)-1))
# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
