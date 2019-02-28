# insertion sort

# in this sort we select the frist element and the next element has to be properly based before or
# after the selected element


def insertion_sort(A):
    """
    :type A: input array or list and this insertion sort is an in-place memory sort which is we are using constant memory.
    """
    for i in range(0, len(A)-1):
        value = A[i+1]
        for j in range(i, -1, -1):
            if value < A[j]:
                A[j+1] = A[j]
                A[j] = value
    return A


z = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(insertion_sort(z))

