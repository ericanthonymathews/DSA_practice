def root(x, n):
    pass  # your code goes here
    l, r = 0, x
    mid = (l + r) / 2.0
    while mid - l >= 0.001:
        y = mid ** n
        if y > x:
            r = mid
        elif y < x:
            l = mid
        else:
            return mid
        mid = (l + r) / 2.0
    return mid

# binary search - log search
# usual: while (l <= r) and (y - root(x,n))
# lo < mid < hi
# while (mid - lo > 0.001):
