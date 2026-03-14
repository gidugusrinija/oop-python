s = "srinija"

rev_str = s[::-1]

res = ""

end = len(s) - 1

for i in range(end, -1, -1):
    res += s[i]


res3 = "".join(reversed(s))


print(res, rev_str, res3)

