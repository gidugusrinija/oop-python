l = [1, 2, 3, 4, 5]
k = 2

arr = l[k:] + l[:k]

print(arr)

k = k % len(arr)

from collections import deque

deq = deque(l)
deq.rotate(-k)

print(list(deq))

n = len(l)


def reverse(arr, l, r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1


reverse(l, 0, k-1)
reverse(l, k, n-1)
reverse(l, 0, n-1)

print(l)


