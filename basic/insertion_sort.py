#Quadratic runtime O(n2)
#Is a slow, but simple algorithm

# With each iteration, it compares the current value with the value on
# the left and if it is smaller, it changes position until it finds a
# larger one, then goes back through the array starting from the current point

# [2, 6, 5, 1, 3, 4]
# [2, 5, 6, 1, 3, 4]
# [2, 5, 1, 6, 3, 4]
# [2, 1, 5, 6, 3, 4]
# [1, 2, 5, 6, 3, 4]
# [1, 2, 5, 3, 6, 4]
# [1, 2, 3, 5, 6, 4]
# ...

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            print(arr)
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    print(arr)


array = [2, 6, 5, 1, 3, 4]
insertion_sort(array)