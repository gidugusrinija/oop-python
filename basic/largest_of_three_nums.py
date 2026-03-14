a, b, c = 11, 9, 10
ls = [11, 9, 10]

max_num = float("-inf")

for i in [a, b, c]:
    if i > max_num:
        max_num = i
print(max_num)