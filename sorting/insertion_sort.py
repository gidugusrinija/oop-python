l = [3, 4, 1, 2, 9, 8, 7]


def insertion_sort(l):
    n = len(l)

    for i in range(1, n):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key

    print(l)
    return l


insertion_sort(l)
