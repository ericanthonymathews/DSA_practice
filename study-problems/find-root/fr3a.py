import numpy as np
# The result(D) is the nth root of x
# K^(1/n)= D
# logn(K^(1/n)) = logn(D)
# (1/n)logn(K) = logn(D)
# D = n^((1/n)logn(K))


def root(k, n):
    return pow(n, ((1.0 / n) *
                   (np.log(k) /
                    np.log(n))))
