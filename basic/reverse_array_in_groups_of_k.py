arr = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3

# op: 3,2,1,6,5,4,8,7

n = len(arr)


for i in range(0, n, k):
    left = i
    right = min(i + k - 1, n - 1)

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
print(arr)


