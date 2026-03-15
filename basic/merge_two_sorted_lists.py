l1 = [1, 4, 6, 0, 0]
l2 = [2, 5]

n = len(l1)  # 5
m = len(l2)  # 2

last = n - 1  # 4

l2_p = m - 1  # 1
l1_p = last - m  # 2

while l2_p >= 0:
    if l1[l1_p] > l2[l2_p]:
        l1[last] = l1[l1_p]
        l1_p -= 1
    else:
        l1[last] = l2[l2_p]
        l2_p -= 1
    last -= 1

del l2

print(l1)


