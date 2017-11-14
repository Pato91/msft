# Packing and unpacking arguments


# UNPACKING ::

lst = [1,2,3,4]

def func(a,b,c,d):
	''' sample func '''
	print( d, c, b, a)

# func() # no args, error
# func(lst) # only one arg, error
func(*lst)


# Example with range ( syntax: range(start, stop, step))
r = [1, 11, 2] # [start, stop, step]

# print( list(range(r)) ) #error, range expects an integer input
print( list(range(r[0], r[1], r[2])) ) #yes?!!! :( :( = sad programmer
print( list(range(*r)) )

# PACKING ::
# When we dont know number of args

def total(*args):
	''' add together a list of arguments '''
	tot = 0
	for arg in args:
		tot += arg

	return tot

print( total(1, 2)) # 3
print( total(1, 2, 3, 4, 5, 6)) # 21

# signature func

# def sig(*args, **kwargs):
# 	''' accepts arbitrary multiple arguments and key-word rguments '''
# 	pass

# UNPACKING A DICT
def kvs(one,two,three):
	print(one, two, three)

d = {"one": 1, "two": 2, "three": 3}
kvs(**d)

def fun(arg, **kwargs):
	''' unknown number of key-word args '''
	print(arg)
	for key in kwargs:
		print( key, kwargs[key])

fun(100, one="one", two="two", three="three")
