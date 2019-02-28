# merge sort is a divide and conquer algorithm where the time complexity reduces but as we are not using the in place
# we are using the extra memory which O(n)

def merge_sort(A):
    if len(A) <= 1:
        return A
    else:
        mid = int(len(A)/2)
        left = A[0:mid]
        right = A[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, A)
    return A

def merge(left, right, B):

    i, j, k = 0, 0, 0
    while (i < len(left)) & (j < len(right)):
        if left[i] < right[j]:
            B[k] = left[i]
            k = k + 1
            i = i + 1
        else:
            B[k] = right[j]
            k = k + 1
            j = j + 1
    while i < len(left):
        B[k] = left[i]
        i = i+1
        k = k+1
    while j < len(right):
        B[k] = right[j]
        j = j+1
        k = k+1

    return B

z = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(merge_sort(z))
