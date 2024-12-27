import numpy as np

bools_to_int = lambda l : sum(x*2**i for i, x in enumerate(reversed(l)))

def power(data):
    s = sum(data)
    gamma = bools_to_int(list(map(lambda x : 2*x > len(data), s)))
    return gamma * (2**len(s) - 1 - gamma)

def data_filter(data, filtr, p = 0):
    if len(data) == 1:
        return bools_to_int(data[0])
    return data_filter(list(filter(
            filtr(sum(x[p] for x in data), len(data), p), data)), filtr, p + 1)

def O2_filtering(s, n, p): return lambda x : x[p] == (2*s >= n)
def CO2_filtering(s, n, p): return lambda x : x[p] == (2*s < n)

data = [np.array(list(map(lambda s : s == '1', line.rstrip())))
                                for line in open("../inputs/03.inp")]

print(power(data))
print(data_filter(data, O2_filtering) * data_filter(data, CO2_filtering))