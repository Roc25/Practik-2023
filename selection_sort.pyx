from cpython cimport array
import array

cpdef int[:] selection_sort(list a_list, int l):
    cdef int i, j, smallest
    cdef array.array a = array.array('l', a_list)
    cdef int[:] x_list = a
    for i in range(0, l - 1):
        smallest = i
        for j in range(i + 1, l):
            if x_list[j] < x_list[smallest]:
                smallest = j
        x_list[i], x_list[smallest] = x_list[smallest], x_list[i]
    return x_list