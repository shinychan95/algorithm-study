def merge_array(a, b):
    index = 0
    for v in a:
        while 1:
            if b[index] < v:
                index += 1
            else:
                b.insert(index, v)
                index += 1
                break
        if index == len(b):
            break
    return b


def merge_sort(arr):
    if len(arr) >= 2:
        return merge_array(merge_sort(arr[:len(arr) // 2]),
                           merge_sort(arr[len(arr) // 2:]))
    else:
        return arr[0]


def cartesian_product_sort(a, b):
    if len(a) >= 2:
        return merge_array(merge_sort(cartesian_product_sort(a[:len(a) // 2], b)),
                           merge_sort(cartesian_product_sort(a[len(a) // 2:], b)))

    else:
        for i, v in enumerate(b):
            b[i] = v*a[0]


T = int(input())

for t in range(T):
    n, m, k = [int(i) for i in input().split(" ")]
    A = sorted([int(j) for j in input().split(" ")])
    B = sorted([int(k) for k in input().split(" ")])

    print(cartesian_product_sort(A, B))

    # print(merge_sort(Arr)[k - 1])


