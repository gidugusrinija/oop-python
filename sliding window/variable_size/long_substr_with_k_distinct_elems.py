st = "abbcdedcecdda"
k = 3

def long_substr(s, k):
    max_len = 0
    st, end = -1, -1
    left = 0
    char_map = {}

    for right, val in enumerate(s):
        char_map[val] = char_map.get(val, 0) + 1

        while len(char_map) > k:
            if char_map[s[left]] == 1:
                del char_map[s[left]]
            else:
                char_map[s[left]] -= 1
            left += 1

        if right - left + 1 > max_len:
            max_len = right - left + 1
            st = left
            end = right + 1

    return max_len, s[st:end]

max_l, res = long_substr(st, k)

print(max_l, res)
