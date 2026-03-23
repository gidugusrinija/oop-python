"""
Longest Substring Without Repeating Characters
Input: String s.

Goal: Find the length of the longest substring without repeating characters.

Example: s = "abcabcbb" → Output: 3 ("abc").
"""


def longest_substring(s):
    left = 0
    max_len = 0
    start, end = -1, -1
    char_map = {}

    for right, val in enumerate(s):
        if val in char_map and char_map[val] >= left:
            left = char_map[val] + 1
        char_map[val] = right
        if right - left + 1 > max_len:
            max_len = right - left + 1
            start = left
            end = right + 1
    return max_len, start, end


s = "abcdefghaxyzwstuvop"
max_l, st, e = longest_substring(s)
print(max_l, s[st:e])
