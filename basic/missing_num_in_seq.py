l = [1, 2, 3, 4, 5, 6, 7, 9]

n = len(l) + 1

xor_all = 0
xor_arr = 0

for i in range(1, n + 1):
    xor_all ^= i

for i in l:
    xor_arr ^= i

print(xor_arr ^ xor_all)
