def move_ones(arr):
    j = 0

    for i in range(len(arr)):
        if arr[i] != 1:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return arr


arr = [1, 5, 2, 1, 3, 1, 4, 1]
print(move_ones(arr))
