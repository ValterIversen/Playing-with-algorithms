# [1, 6, 5, 2, 3, 4]
# [1, 2, 5, 6, 3, 4]
# [1, 2, 3, 6, 5, 4]
# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6]


def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[cur_min_index]:
                cur_min_index = j
        arr[i], arr[cur_min_index] = arr[cur_min_index], arr[i]
        print(arr)



array = [2, 6, 5, 1, 3, 4]
selection_sort(array)