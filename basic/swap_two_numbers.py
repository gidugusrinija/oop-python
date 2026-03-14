n1 = 5
n2 = 6

# without temp
print(n1, n2)

n1, n2 = n2, n1

print(n1, n2)

# with temp
temp = n1
n1 = n2
n2 = temp

del temp

print(n1, n2)
