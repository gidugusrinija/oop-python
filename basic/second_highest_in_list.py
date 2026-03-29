l = [100, 100, 100]


def find_sec_highest(l):
    first_max = 0
    second_max = 0

    for i in l:
        if i > first_max:
            second_max = first_max
            first_max = i

        elif first_max > i > second_max:
            second_max = i

    return second_max


print(find_sec_highest(l))
