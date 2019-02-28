#selection sort

#in this sort we select the least of the numbers and swap it with the first elements consecutively
#if there Are n elements then
#1st iteration ---> n-1 comparisions and 1 swap (n)
#2nd iteration ---> since the first one is sorted we have to do for n-1 elements which has n-2 comparisions and 1 swap total (n-1)
#....
#...
#...
#n-1 iteration ---> 1 comparision and 1 swap


def selection_sort(A):
    """
    :type A: input array or list and this selection sort is an in-place memory sort which is we are using constant memory.
    """
    k = 0
    while k < len(A)-2:
        point = k
        for i in range(k, len(A)-1):
            if A[point] > A[i+1]:
                point = i+1
        #swapping after every iteration
        p = A[k]
        A[k] = A[point]
        A[point] = p
        k = k + 1
        print(A)
    return A


z = [9,8,7,6,5,4,3,2,1]
print(selection_sort(z))


