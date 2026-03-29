rot_arr = [5, 7, 8, 1, 2, 3]
t = 8

def find_element(rot_arr, t):
    low = 0
    high = len(rot_arr) - 1

    while low <= high:
        mid = (low + high)//2
        if rot_arr[mid] == t:
            return mid

        # find the side for sorted array( left or right from mid)

        if rot_arr[low] <= rot_arr[mid]:
            if rot_arr[low] <= t < rot_arr[mid]:
                high -= 1
            else:
                low += 1
        else:
            if rot_arr[mid] < t <= rot_arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

print(find_element(rot_arr, t))
