l1 = [-1, 3, 4, 8, 0, 0, 0]

l2 = [2, 7, 9]


def merge_two_sorted_arrs(l1, l2):
    m, n = len(l1), len(l2)

    l1_high = m - 1

    l2_p = n - 1

    l1_p = m - n - 1

    while l2_p >= 0:
        if l1[l1_p] > l2[l2_p]:
            l1[l1_high] = l1[l1_p]
            l1_p -= 1
        else:
            l1[l1_high] = l2[l2_p]
            l2_p -= 1
        l1_high -= 1
    return l1


print(merge_two_sorted_arrs(l1, l2))
