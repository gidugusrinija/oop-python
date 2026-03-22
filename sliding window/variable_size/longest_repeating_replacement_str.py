"""
Longest Repeating Character Replacement
Input: String s and integer k.

Goal: You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times. Find the longest substring containing the same letter.

Example: s = "AABABBBBBBA", k = 1 → Output: 4 (Replace 'B' at index 2 to get "AAAA")
"""


def long_substring(s, k):
    leaders_count = 0
    max_len = 0
    char_map = {}
    left = 0
    st, end = -1, -1

    for right, val in enumerate(s):
        char_map[val] = char_map.get(val, 0) + 1

        leaders_count = max(leaders_count, char_map[val])

        while (right - left + 1 - leaders_count) > k:
            char_map[s[left]] -= 1
            left += 1

        if (right - left + 1) > max_len:
            max_len = right - left + 1
            st = left
            end = right

    return max_len, st, end


s = "AABABBBBBBA"
k = 2
m, start, e = long_substring(s, k)
print(m, s[start:e+1])
