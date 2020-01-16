
def find_sqrt_n(n, tolerance_level=.01):

    lower_bound = n / 2
    upper_bound = lower_bound

    while (lower_bound)**2 > n:

        upper_bound = lower_bound
        lower_bound = lower_bound / 2

    new_bound = lower_bound + (upper_bound - lower_bound)/2
    sqrt_n_sqrd = new_bound**2

    while abs(sqrt_n_sqrd - n) > tolerance_level:

        if sqrt_n_sqrd > n:
            upper_bound = new_bound
        else:
            lower_bound = new_bound

        new_bound = lower_bound + (upper_bound - lower_bound) / 2
        sqrt_n_sqrd = new_bound ** 2

#    return (upper_bound, lower_bound, new_bound)
    return new_bound


assert abs(find_sqrt_n(400)**2 - 400) < .01
assert abs(find_sqrt_n(4)**2 - 4) < .01
assert abs(find_sqrt_n(0)**2 - 0) < .01
assert abs(find_sqrt_n(45)**2 - 45) < .01 