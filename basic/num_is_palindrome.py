num = 12321

rev = 0

org = num
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print(org == rev)
print(org.__eq__(rev))
print(org is rev)  # return False even for palindrome
