n = 10001

rem = n % 2 # using modulus
rem2 = n & 1 # using AND

# using modulus
if not (rem & rem2):
    print("Even")
else:
    print("Odd")
