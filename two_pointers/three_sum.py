"""
1. sort the array
2. fix Pointer i
3. now find j, k pointers
repeat until we found the reqd sum
"""


l = [1, 0, -2, -6, 5, 4, 3, 9, 4]
t = 3

def three_sum(l, t):
    l = sorted(l)
    i = 0
    n = len(l)
    res = set()

    while i < n-2:
        j = i + 1
        k = n - 1
        reqd_sum = t - l[i]
        while j < k:
            curr_sum = l[j] + l[k]

            if reqd_sum == curr_sum:
                res.add((l[i], l[j], l[k]))
                j += 1
                k -= 1
            elif curr_sum > reqd_sum:
                k -= 1
            else:
                j += 1
        i += 1

    return res

print(three_sum(l, t))
