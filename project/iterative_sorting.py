# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr
             


# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        
        for j in range(i,0,-1):
            
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr



# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    swap_instance = True
    while swap_instance:
        swap_instance = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                # swap
                index = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = index
                swap_instance = True

    return arr

arr = [5,4,3,5,7,9,20,12,34,57]
print(arr)

arr = bubble_sort(arr)
print(arr)

# STRETCH: implement the Count Sort function below
def count_sort(arr): 
    if len(arr) == 0:
        return arr
    
    maximum = max(arr) #declaring the highest value in the array

    count = [0] * (maximum+1) #creating the 'count array'. The +1 is added so that the tallies will be at an index that's the same as the actual value of the ref number in the original array.  
    for value in arr:
        if value < 0:
            return False #not allowing negative values
        else:
            count[value] += 1 #adding 1 tally for each instance of a number 

    for i in range(1,len(count)): #Iterating over the 'count array': Replacing each number with the sum of itself and its predecessor. After this, each # in the arr will represent the sorted location of the value of its index.
        count[i] += count[i-1]
    
    sorted_arr = [0] * len(arr) #creating a new sorted array

    for i in range(0, len(arr)):
        count_index = arr[i]
        sorted_index = count[count_index]
        sorted_arr[sorted_index-1] = count_index 
        count[count_index] -= 1

    
    return arr

arr = [5,4,3,5,7,9,20,12,34,57]

arr = count_sort(arr)