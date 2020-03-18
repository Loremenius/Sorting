# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for index in range(elements):
        if len(arrA) > 0 and len(arrB) > 0:
            if arrA[0] < arrB [0]:
                merged_arr[index] = arrA[0]
                arrA.pop(0)
            else:
                merged_arr[index] = arrB[0]
                arrB.pop(0)
        elif len(arrA) > 0:
            merged_arr[index] = arrA[0]
            arrA.pop(0)
        else:
            merged_arr[index] = arrB[0]
            arrB.pop(0)
    # for item in arrA:
    #     merged_arr[index] = item
    #     index += 1
    
    # for item in arrB:
    #     merged_arr[index] = item
    #     index += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        arr = merge(merge_sort(left), merge_sort(right))

    return arr

print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
