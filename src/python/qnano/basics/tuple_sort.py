
d = dict()

d["a"] = 2
d["b"] = 1
d["d"] = 0

list_of_tuples = list(d.items())

list_of_tuples.sort(key=lambda x:x[1])

print(list_of_tuples)

# flatten list
# converting 2d list into 1d
# using functools.reduce
from functools import reduce
ini_list = [[1, 2, 3],
            [3, 6, 7],
            [7, 5, 4]]
flatten_list = reduce(lambda z, y :z + y, ini_list)
flatten_list = sum(ini_list, [])
flatten_list = [j for sub in ini_list for j in sub]

# int to binary
bin_37 = "{0:b}".format(37)
bin_10 = bin(10)
# '0b1010'

# collections.deque
# zip
# regex
# collections - namedtuple
# clean python
# string functions
# fibonacci
# itertools
# functools

# docker - millstein
# cicd

# stl:
# https://docs.python.org/3/library/
# statistics

# scikitlearn
# tensorflow2: mnist

# rigetti
# materials project


