
s1 = "apple"
s2 = "panple"

# space optimized approach

ch_map = {}

if len(s1) != len(s2):
    print("Not an Anagram")
else:
    for i in s1:
        ch_map[i] = ch_map.get(i, 0) + 1

    for i in s2:
        if i not in ch_map:
            print("Not an Anagram")
            break
        ch_map[i] -= 1

        if ch_map[i] == 0:
            del ch_map[i]
    else:
        print("Anagram")
