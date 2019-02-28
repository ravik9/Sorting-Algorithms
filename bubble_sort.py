# Bubble sort
# In this sort we compare the two adjacent elements and if the lower position of the element is greater than the
# upper position of comparing then we swap them.
# by end of each iteration the largest elemnents get their correct position in the array
# time complexity is O(n^2) which is same as selection sort too.


def bubble_sort(A):
    """
    :type A: input array or list and this bubble sort is an in-place memory sort which is we are using constant memory.
    """


    k = 0
    print(len(A))
    for i in range(0, len(A)-1):
        for j in range(0, len(A)-1-i):
            if A[j] > A[j+1]:
                # if greater than the previous one just swap
                k = A[j]
                A[j] = A[j+1]
                A[j+1] = k
        print(A)
    return A


z = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(bubble_sort(z))

