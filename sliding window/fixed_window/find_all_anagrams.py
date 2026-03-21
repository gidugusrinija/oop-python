s = "cbaebabacdabcab"
p = "abc"


def approach1(s, p):
    k = len(p)
    char_map = {}
    res = []

    for i in p:
        char_map[i] = char_map.get(i, 0) + 1

    from copy import deepcopy
    for i in range(len(s)):
        ref_map = deepcopy(char_map)
        wind_str = s[i:i+k]
        if len(wind_str) != k:
            break
        for j in wind_str:
            if j not in ref_map:
                break
            ref_map[j] -= 1

            if ref_map[j] == 0:
                del ref_map[j]

        if len(ref_map) == 0:
            res.append(i)
    return res

# using sliding window

def find_anagrams(s, p):
    res = []
    l_s, l_p = len(s), len(p)

    if l_p > l_s:
        return res
    p_map = {}
    for i in p:
        p_map[i] = p_map.get(i, 0) + 1

    s_map = {}

    for i in range(l_p):
        s_map[s[i]] = s_map.get(s[i], 0) + 1

    if s_map == p_map:
        res.append(0)

    for i in range(l_p, l_s):
        right_char = s[i]

        left_char = s[i - l_p]

        s_map[right_char] = s_map.get(right_char, 0) + 1

        if left_char in s_map:

            if s_map[left_char] == 1:
                del s_map[left_char]
            else:
                s_map[left_char] -= 1

        if s_map == p_map:
            res.append(i-l_p+1)
    return res


print(find_anagrams(s, p))
print(approach1(s, p))

















