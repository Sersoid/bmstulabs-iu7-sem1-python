def bubble_sort(array):
    array_len = len(array)
    for i in range(1, array_len):
        for j in range(array_len - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


input_array = [int(i) for i in input().split()]
print(bubble_sort(input_array))
