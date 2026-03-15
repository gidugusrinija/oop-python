l = [3, 4, 1, 2, 9, 8, 7]


def selection_sort(l):
    n = len(l)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if l[j] < l[min_idx]:
                min_idx = j
        l[i], l[min_idx] = l[min_idx], l[i]

    print(l)

    return l


selection_sort(l)