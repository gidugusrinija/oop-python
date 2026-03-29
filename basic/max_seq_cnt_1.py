l = "00111100000011111110000011"


def max_seq_one(s):
    cnt = 0

    st, end = -1, -1

    max_cnt = 0

    for idx, i in enumerate(s):
        if i == "1":
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
                st = idx - cnt + 1
                end = idx
        else:
            cnt = 0

    return max_cnt, s[st:end+1]


print(max_seq_one(l))
