def bubble_sort(array):
    n = len(array)
    
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

int_array = [1,9,2,8,3,7,4,6,5]

var = 0

while var <= 8:              
    print("Old variable value :", int_array[var])
    var = var + 1
print("")
bubble_sort(int_array)

print("")

var = 0

while var <= 8:              
    print("New variable value :", int_array[var])
    var = var + 1
    
print("")
print("#########################")
print("")