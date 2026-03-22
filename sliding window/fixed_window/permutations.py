"""Input: Strings s1 and s2.

Goal: Return true if s2 contains a permutation of s1.

Example: s1 = "ab", s2 = "eidbaooo" → Output: True (contains "ba")."""


def find_permutations(s1, s2):

    m, n = len(s1), len(s2)

    s1_map = {}
    for i in s1:
        s1_map[i] = s1_map.get(i, 0) + 1

    s2_map = {}
    for i in range(m):
        s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1

    if s1_map == s2_map:
        return True

    for i in range(m, n):
        right_char = s2[i]
        left_char = s2[i - m]

        s2_map[right_char] = s2_map.get(right_char, 0) + 1

        if s2_map[left_char] == 1:
            del s2_map[left_char]
        else:
            s2_map[left_char] -= 1

        if s1_map == s2_map:
            return True
    return False


s1 = "abc"
s2 = "eidaooocba"
print(find_permutations(s1, s2))
