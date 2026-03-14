s = 100033456789

# using while loop

s1 = s
sum1 = 0
while s1 > 0:
    digit = s1 % 10
    sum1 += digit
    s1 = s1 // 10

print(sum1)


# using recursion

def find_sum(n):
    if n == 0:
        return 0

    sum2 = n % 10 + find_sum(n // 10)

    return sum2


s2 = s
print(find_sum(s2))

# using type conversion
s3 = str(abs(s))

sum3 = 0
for i in s3:
    sum3 += int(i)
print(sum3)
