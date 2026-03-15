nested_list = [[1, 2, 3], [[4, 5, 6, 9], [8, 11], [12, 3, [14]]]]

res = []


def flatten(l):
    for i in l:
        if isinstance(i, list):
            flatten(i)
        else:
            res.append(i)
    return res


print(flatten(nested_list))


