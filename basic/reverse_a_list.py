ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]


right = len(ls) - 1

end = len(ls) // 2

for left in range(end):
    ls[left], ls[right] = ls[right], ls[left]
    right -= 1

print(ls)
