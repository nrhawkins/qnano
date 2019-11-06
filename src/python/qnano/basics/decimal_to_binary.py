
def decimal_to_binary_helper(n, l):

    l.append(str(n % 2))

    if n > 1:
        decimal_to_binary_helper(n // 2, l)
    else:
        pass

    return l

def decimal_to_binary(n):

    l = decimal_to_binary_helper(n, list())

    l.reverse()

    binary_string = "".join(l)

    return binary_string


assert decimal_to_binary(5) == "101"
assert decimal_to_binary(4) == "100"
assert decimal_to_binary(3) == "11"
assert decimal_to_binary(2) == "10"
assert decimal_to_binary(1) == "1"
assert decimal_to_binary(0) == "0"

