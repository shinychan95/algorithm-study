def insert_value(arr, v):
    index = 0
    while 1:
        if index == len(arr):
            arr.insert(index, v)
            break
        if arr[index][0] < v[0] or (arr[index][0] == v[0] and arr[index][1] < v[1]):
            index += 1
        else:
            arr.insert(index, v)
            index += 1
            break
    return arr


def binary_search_insert(arr, v):
    start = 0
    end = len(arr) - 1
    while 1:
        if end == -1:
            arr.append(v)
            break
        if end == start:
            if arr[end][0] < v[0] or (arr[end][0] == v[0] and arr[end][1] < v[1]):
                arr.append(v)
            else:
                arr.insert(end, v)
            break
        middle = start + (end - start) // 2
        if arr[middle][0] < v[0]:
            start = middle + 1
        elif arr[middle][0] == v[0]:
            if arr[middle][1] < v[1]:
                start = middle + 1
            else:
                end = middle
        else:
            end = middle
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    equal = []
    right = []

    for v in arr:
        if v < pivot:
            left.append(v)
        elif v > pivot:
            right.append(v)
        else:
            equal.append(v)

    return quick_sort(left) + equal + quick_sort(right)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result


def sort_one_by_one(a, b, n):
    arr = [[v*b[0], i, 0] for i, v in enumerate(a)]
    n -= 1
    for i in range(n):
        if arr[0][2] == len(b) - 1:
            del arr[0]
            n -= 1
            continue
        tmp = [a[arr[0][1]]*b[arr[0][2] + 1], arr[0][1], arr[0][2] + 1]
        del arr[0]
        arr = binary_search_insert(arr, tmp)

    return arr[0][0]

def sort_one_by_one2(a, b, n):
    arr = [[v*b[0], i, 0] for i, v in enumerate(a)]
    n -= 1
    for i in range(n):
        if arr[0][2] == len(b) - 1:
            del arr[0]
            n -= 1
            continue
        tmp = [a[arr[0][1]]*b[arr[0][2] + 1], arr[0][1], arr[0][2] + 1]
        del arr[0]
        arr = binary_search_insert(arr, tmp)

    return arr[0][0]


T = int(input())

for t in range(T):
    n, m, k = [int(i) for i in input().split(" ")]
    A = sorted([int(i) for i in input().split(" ")])
    B = sorted([int(i) for i in input().split(" ")])

    Arr = [[v * B[0], i, 0] for i, v in enumerate(A)]
    _k = k

    _k -= 1
    for i in range(_k):
        if Arr[0][2] == len(B) - 1:
            del Arr[0]
            _k -= 1
            continue
        temp = [A[Arr[0][1]] * A[Arr[0][2] + 1], Arr[0][1], Arr[0][2] + 1]
        del Arr[0]
        Arr = binary_search_insert(Arr, temp)
