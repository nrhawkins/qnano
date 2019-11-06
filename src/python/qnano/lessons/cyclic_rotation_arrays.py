
def find_cyclic_rotation(A, K):

    B = A.copy()

    if not A or K == 0:
        return A
    else:
        for i in range(len(A)):
            B[(i + K) % len(A)] = A[i]

    A = B

    return A

assert find_cyclic_rotation([], 4)  == []

assert find_cyclic_rotation([1,2,3,4], 4) == [1,2,3,4]

assert find_cyclic_rotation([1,2,3,4], 1) == [4,1,2,3]

assert find_cyclic_rotation([1,2,3,4], 0) == [1,2,3,4]

assert find_cyclic_rotation([1,2,3,4], 100) == [1,2,3,4]

assert find_cyclic_rotation([1,2,3,4], 99) == [2,3,4,1]

assert find_cyclic_rotation([-1000,1000,-1000], 1) == [-1000,-1000,1000]

assert find_cyclic_rotation([-1000,1000,-1000], 3) == [-1000,1000,-1000]


# empty array
# one element
# two elements
# small functional tests, K < N
# small functional tests, K >= N
# small random sequence, all rotations, N = 15
# medium random sequence, N = 100
# maximal N and K

