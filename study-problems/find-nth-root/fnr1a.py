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
    '''
  input: float, integer
  output: integer
  edgecases:
  outliers:
  y^n = x

  input: x:7 n:3
  l:0
  r:6
  m:3
  m = (l + r / 2)
  27
  r = m
  l:0
  r:3
  m:1.5
  m = (l + r / 2)
  1^3->3.375
  l = m
  l:1.5
  r:3
  m:2.25
  m = (l + r / 2)
  2.25^3->3.375
  l = m
  ...
  y^n = x
  if abs(y - root(x,n)) < 0.001
  '''

# binary search - log search
# usual: while (l <= r) and (y - root(x,n))
# lo < mid < hi
# while (mid - lo > 0.001):
