l = [1, 2, 3, 4, 5]
k = 2

# slicing  approach
k_1 = k % len(l)

new = l[-k:] + l[:-k]

print(new)

# using deque

from collections import deque

dq = deque(l)
dq.rotate(2)

print(list(dq))

# in place
n = len(l)


def reverse(start, end, arr):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


reverse(0, n - 1, l)
reverse(0, k_1 - 1, l)
reverse(k_1, n - 1, l)

print(l)
