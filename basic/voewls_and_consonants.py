word = "apple"

vowels = "aeiouAEIOU"

v_cnt = 0
c_cnt = 0

for i in word:
    if i.isalpha():
        if i in vowels:
            v_cnt += 1
        else:
            c_cnt += 1
print(v_cnt, c_cnt)
