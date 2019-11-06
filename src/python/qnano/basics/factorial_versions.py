import math

def factorial(n):

    if not isinstance(n, int):
        raise ValueError("n must be an int")
    elif n < 0:
        raise ValueError("n must be > 0")

    if n == 1:
        return n
    else:
        return n*factorial(n-1)


assert factorial(8) == math.factorial(8)

def factorial_loop(n):

    factorial = 1

    for n in range(1, n+1):
        factorial = factorial*n

    return factorial

assert factorial_loop(18) == math.factorial(18)

n=10
#print(f"factorial (n={n}", factorial(n))
print(f"factorial loop (n={n})", factorial_loop(n))

factorial(-5)
#factorial(3.2)
#factorial("a")

#import pytest
#with pytest.raises(ValueError) as excinfo:
#    assert "n must be an int > 0" in str(excinfo.value)
