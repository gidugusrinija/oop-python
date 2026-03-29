inputs = ["ate", "xob", "eAt", "tea", "box", "pen"]
from collections import defaultdict


def group_anagrams(inputs):
    groups = defaultdict(list)

    for input_ in inputs:
        res = "".join(sorted(input_.lower()))

        groups[res].append(input_)

    return list(groups.values())


def using_freq_map(inputs):
    grps = defaultdict(list)

    for word in inputs:
        cnt = [0] * 26
        for ch in word:
            cnt[ord(ch.lower()) - ord('a')] += 1
        grps[tuple(cnt)].append(word)

    return list(grps.values())


print(using_freq_map(inputs))
print(group_anagrams(inputs))
