import time

ls = [2, 1, 5, 19, 3, 20, 114]
k = 3


# Brute force

def max_subarray_sum_with_size_k(ls, k):
    start_time = time.perf_counter()
    max_sum = 0
    stt, endd = -1, -1
    for i in range(0, len(ls)):
        itr = i
        curr_sum = 0
        while itr-i < k and itr < len(ls):
            curr_sum += ls[itr]
            itr += 1
        if curr_sum > max_sum:
            stt = i
            endd = itr
            max_sum = curr_sum

    end_time = time.perf_counter()
    print(f"Total processing time for max_subarray_sum_with_size_k: {end_time - start_time:.6f}s")
    return max_sum, stt, endd


# using sliding window
def max_sub_array(ls, k):
    start_time = time.perf_counter()
    window_sum = sum(ls[:k])
    max_sum = window_sum
    s, e = 0, k-1

    for idx, val in enumerate(ls[k:], start=k):
        window_sum += val - ls[idx - k]

        if window_sum > max_sum:
            max_sum = window_sum
            s = idx - k + 1
            e = idx
    end_time = time.perf_counter()
    print(f"Total processing time for max_sub_array: {end_time-start_time:.6f}s")
    return max_sum, s, e


max_s, st, end = max_subarray_sum_with_size_k(ls, k)
print(max_s, ls[st:end])

print("------------------------------------------")

max_summ, s1, e1 = max_sub_array(ls, k)
print(max_summ, ls[s1:e1+1])
