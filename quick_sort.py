def quick(a, start, end):
    pindex, i = 0, 0
    while i <= end -1:
        if a[i] < a[end]:
            k = a[pindex]
            a[pindex] = a[i]
            a[i] = k
            i = i + 1
            pindex = pindex + 1
        else:
            i = i + 1
    # swap the pindex and the end which is a pivot here after the whole array iteration
    k = a[end]
    a[end] = a[pindex]
    a[pindex] = k
    print(a)
    return pindex


def quick_sort(a, start, end):

    if start < end:
        pivot_position = quick(a, start, end)
        quick_sort(a, 0, pivot_position-1)
        quick_sort(a, pivot_position+1, end)


z = [8,3,1,2,6,7,4]
quick_sort(z, 0, len(z)-1)
print(z)

