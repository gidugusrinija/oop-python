def rev_string(s):
    if len(s) == 0:
        return s
    return rev_string(s[1:]) + s[0]


stri = "srinija"

print(rev_string(stri))

