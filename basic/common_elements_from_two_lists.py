l1 = [1, 3, 4, 7, 7, 9, 10, 2, 5]
l2 = [9, 4, 6, 8, 2, 1, 1, 8]

seen = set()
for i in l1:
    if i not in seen:
        seen.add(i)

res = set()
for i in l2:
    if i in seen:
        res.add(i)

print(list(res))


print(list(set(l1) & set(l2)))
print(list(set(l1).intersection(set(l2))))

