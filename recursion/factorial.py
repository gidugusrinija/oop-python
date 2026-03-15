
memo = {0: 1, 1: 1}


def fact(i):
    if i <= 1:
        return memo[i]
    memo[i] = i * fact(i-1)
    return memo[i]


print(fact(5))

