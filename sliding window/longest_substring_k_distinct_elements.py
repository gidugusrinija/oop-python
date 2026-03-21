st = "abbcdedcecdda"
k = 3


def long_substring_with_k(st, k):
    max_l = 0
    stt = 0
    left = 0
    char_map = {}
    for right in range(len(st)):
        char_map[st[right]] = char_map.get(st[right], 0) + 1
        while len(char_map) > k:
            char_map[st[left]] -= 1
            if char_map[st[left]] == 0:
                del char_map[st[left]]
            left += 1
        if (right - left) + 1 > max_l:
            stt = left
            max_l = right - left + 1
    return stt, max_l


start, max_len = long_substring_with_k(st, k)

print("max len: ", max_len)
print("str: ", st[start: start + max_len])
