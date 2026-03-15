l = [3, 4, 1, 2, 9, 8, 7]


def bubble_sort(l):
    n = len(l)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True

        if not swapped:
            break

    print(l)
    return l


bubble_sort(l)
