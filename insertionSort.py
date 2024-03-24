def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        x = arr[i]
        j = i
        while j>0 and arr[j-1]>x:
            arr[j] = arr[j-1]
            j-=1

        arr[j] = x

    return arr





