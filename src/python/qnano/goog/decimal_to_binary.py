
def decimal_to_binary(n, l):

    if n > 1:
        decimal_to_binary(n // 2, l)

    print(n % 2, n)

    l.append(n % 2)

    return l


l = decimal_to_binary(2, list())

print()
print("binary: ", str(l))

