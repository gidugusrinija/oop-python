def find_sum(n):
    if n == 0:
        return 0

    sum2 = n % 10 + find_sum(n // 10)

    if sum2 > 9:
        sum2 = find_sum(sum2)

    return sum2


s2 = 122345679804337918
print(find_sum(s2))