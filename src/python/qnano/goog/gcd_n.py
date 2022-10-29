import math

def gcd_n(num, arr):

    gcd = math.gcd(arr[0], arr[1])

    for i in range(2, len(arr)):

        gcd = math.gcd(gcd, arr[i])

    return gcd


num = 5
#arr = [1,2,3,4,5]
arr = [2,4,6,8,10]

print("out:", gcd_n(num, arr))