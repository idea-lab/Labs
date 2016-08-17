def swap(array, i, j):
    tmp=array[i]
    array[i]=array[j]
    array[j]=tmp

def testSortingAlgorithm(unsort_arr, algorithm):
    print("\nAlgorithm:", algorithm.__name__, "\n")
    print("Unsorted list", unsort_arr, "\n")
    sorted_arr = algorithm(unsort_arr)
    print("Sorted list", sorted_arr, "\n")
    print("##########################################\n")

def bubble_sort(array): # O(n^2)
    work_arr=array[:] #copies array
    n = len(work_arr)
    for pass_num in range (0, n-1): #guaranteed to be sorted after n-1 passes
        for i in range(1, n-pass_num):
            if work_arr[i-1] > work_arr[i]:
                swap(work_arr, i, i-1)
    return work_arr

def insertion_sort(array):
    work_arr=array[:]
    for start in range(1, len(work_arr)):
        i=start
        while i>0 and work_arr[i]<work_arr[i-1]:
            swap(work_arr, i, i-1)
            i = i-1
    return work_arr

def selection_sort(array):
    work_arr=array[:]
    for i in range(0, len(work_arr)):
        minIndex=i
        for j in range(i, len(work_arr)):
            if(work_arr[minIndex]>work_arr[j]):
                minIndex=j
        swap(work_arr, minIndex, i);
    return work_arr

testing_array = [1, 9, 2, 8, 3, 7, 4, 6, 5]

testSortingAlgorithm(testing_array, bubble_sort)

testSortingAlgorithm(testing_array, insertion_sort)

testSortingAlgorithm(testing_array, selection_sort)


# var = 0

# while var <= 8:              
#     print("Old variable value :", int_array[var])
#     var = var + 1
# print("")
# bubble_sort(int_array)

# print("")

# var = 0

# while var <= 8:              
#     print("New variable value :", int_array[var])
#     var = var + 1
    
# print("")
# print("#########################")
# print("")


def old_bubble_sort(array):
    n=len(array)

    while n != 0:
        new_n = 0;
        
        for i in range (1, n):
            if array[i-1] > array[i]:
                temp = array[i]
                array[i] = array[i-1]
                array[i-1] = temp
                new_n = n;
                print( ', '.join(str(x) for x in array))
        n = new_n    
    return