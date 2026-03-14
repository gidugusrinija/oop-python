s = "madSDdam"

left = 0
right = len(s) - 1

while left <= right:
    if s[left] != s[right]:
        print("NOT PALINDROME")
        break
    left += 1
    right -= 1
else:
    print("PALINDROME")

