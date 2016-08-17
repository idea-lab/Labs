def swap(array, i, j):
    tmp=array[i]
    array[i]=array[j]
    array[j]=tmp

def testSortingAlgorithm(test_arrays, algorithm):
    for i in range(0, len(test_arrays)):
        print("\nAlgorithm:", algorithm.__name__, "\n")
        print(test_arrays[i][0], ":\n")
        print("Unsorted list", test_arrays[i][1:], "\n")
        sorted_arr = algorithm(test_arrays[i][1:])
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
        print("Swapping ", work_arr[minIndex], " with ", work_arr[i], "\n")
        swap(work_arr, minIndex, i);
        print(work_arr, "\n")
    return work_arr

def merge(left, right):
    result=[]
    while left and right:
        if(left[0]<right[0]):
            result.append(left[0])
            left=left[1: ]
        else:
            result.append(right[0])
            right=right[1:]
    while left:
        result.append(left[0])
        left = left[1: ]
    while right:
        result.append(right[0])
        right=right[1:]
    print("Merged into: ", result, "\n")
    return result

def merge_sort(array):
    if (len(array)<=1):
        return array
    left=[]
    right=[]
    for i in range(0, len(array)):
        if(i%2==1):
            left.append(array[i])
        else:
            right.append(array[i])
    print("Split array into: ", left, " ", right, "\n")
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def quick_sort(array):

def partition(array, start, end):

random_case = ["random case", 1, 9, 2, 8, 3, 7, 4, 6, 5]
best_case = ["best case", 1, 2, 3, 4, 5, 6, 7, 8, 9]
worst_case = ["worst case", 9, 8, 7, 6, 5, 4, 3, 2, 1]

test_cases=[random_case, best_case, worst_case]

testSortingAlgorithm(test_cases, bubble_sort)

testSortingAlgorithm(test_cases, insertion_sort)

testSortingAlgorithm(test_cases, selection_sort)

testSortingAlgorithm(test_cases, merge_sort)

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