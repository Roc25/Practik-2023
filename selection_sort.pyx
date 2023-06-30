def selection_sort(list x_list):
    cdef int i, j, smallest
    for i in range(0, len(x_list) - 1):
        smallest = i
        for j in range(i + 1, len(x_list)):
            if x_list[j] < x_list[smallest]:
                smallest = j
        x_list[i], x_list[smallest] = x_list[smallest], x_list[i]
    return x_list