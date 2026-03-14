word = "srinija"

res = ""

seen = set()

for i in word:
    if i not in seen:
        res += i
        seen.add(i)

print(res)
