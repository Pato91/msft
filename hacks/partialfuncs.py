from functools import partial
# partial functions

def func(a,b,c,d):
    ''' sums the arguments a, b, c and d '''
    return a+b+c+d

print(func(1,2,3,4)) # 10

p = partial(func, 1,2,3) # a partial function with args a,b,c of func fixed as 1,2,3

print( p(6) ) # 12, arg d=6

Q = partial(func, c=10, d=10)  # specific fixing

print( Q(60, 20) ) # 100, arg a=60 and b = 20

# or

P = partial(func, a=10, c=10) # specific fixing

print( P(b=60, d=20) ) # 100, arg b=60 and d = 20
