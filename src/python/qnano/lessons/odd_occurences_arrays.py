
def find_unpaired_integer(A):

    unpaired_set = set()

    for i in A:
        if i in unpaired_set:
            unpaired_set.remove(i)
        else:
            unpaired_set.add(i)

    if len(unpaired_set) == 1:
        return unpaired_set.pop()
    else:
        raise ValueError(f"A does not meet the assumptions.")




assert find_unpaired_integer([1]) == 1
assert find_unpaired_integer([1,2,2,3,1]) == 3

assert find_unpaired_integer([1000000000,2,3,2,3]) == 1000000000

a = [1 for i in range(1000001)]
a[55555] = 0

assert find_unpaired_integer(a) == 0



