l1 = [1, -2, 3, 4, -6, 5, -7, 1, 7]
l = [0, 5, 0, 0 , 0]
k = 5


def max_subarray(l, k):
    left = 0
    max_len = 0

    st, end = -1, -1

    curr_sum = 0
    for right, val in enumerate(l):
        curr_sum += val

        if right - left + 1 > max_len and curr_sum == k:
            max_len = right - left + 1
            st = left
            end = right

        while curr_sum > k:
            curr_sum -= l[left]
            left += 1

    return max_len, l[st:end + 1]


print(max_subarray(l, k))
