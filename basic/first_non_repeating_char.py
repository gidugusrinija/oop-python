word = "tnbprogtramming"

visited_map = {}

for i in word:
    visited_map[i] = visited_map.get(i, 0) + 1

for k, v in visited_map.items():
    if v == 1:
        print(k)
        break





