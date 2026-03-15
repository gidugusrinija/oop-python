ls = [1, 3, 6, 4, 5, 6, 7, 8, 9, 1, 2, 3, 9, 5, 0, 1, 2]

ls1 = [1, 1, 1, 3, 3, 6, 6, 8, 8, 9]  # sorted

seen = set()

res = []

for i in ls:
    if i not in seen:
        res.append(i)
        seen.add(i)
print(res)

ls = sorted(ls)


def remove_duplicates(ls1: list):
    # in-place
    i = 0
    for j in range(1, len(ls1)):
        if ls1[i] != ls1[j]:
            i += 1
            ls1[i] = ls1[j]

    del ls1[i+1:]
    return ls1


print(remove_duplicates(ls))
print(remove_duplicates(ls1))
