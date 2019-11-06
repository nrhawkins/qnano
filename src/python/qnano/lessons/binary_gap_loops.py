

def find_largest_binary_gap(n):

    n_binary = bin(n)[2:]

    longest_binary_gap = 0

    i = 0
    while i < len(n_binary) - 1:

        if n_binary[i] == "1":

            binary_gap = 0
            gap_index = i+1

            while n_binary[gap_index] == "0" and gap_index < len(n_binary) - 1:
                binary_gap += 1
                gap_index += 1

            if n_binary[gap_index] != "1":
                binary_gap = 0

            if binary_gap > longest_binary_gap:
                longest_binary_gap = binary_gap

            i = gap_index

        else:
            i += 1

    return longest_binary_gap


assert find_largest_binary_gap(5) == 1
assert find_largest_binary_gap(8) == 0
assert find_largest_binary_gap(18) == 2

assert find_largest_binary_gap(32) == 0
assert find_largest_binary_gap(1041) == 5

assert find_largest_binary_gap(2147483647) == 0

assert find_largest_binary_gap(529) == 4
assert find_largest_binary_gap(20) == 1
assert find_largest_binary_gap(15) == 0