
def reverse_string(s):

    sl = list(s)

    left = 0
    right = len(s) - 1

    while left < right:
        temp = sl[left]
        sl[left] = sl[right]
        sl[right] = temp
        left += 1
        right -= 1

    return "".join(sl)


print("hello", reverse_string("hello"))