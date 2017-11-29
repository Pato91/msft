# import math

def numchar(begin, end):
	begin = ord(begin)
	end = ord(end)
	print("{0:b}".format(begin), "{0:b}".format(end))
	# print(str(bin(begin)), str(bin(end)))
	# print("{0:b}".format(diff))


numchar('j', 'm')
numchar('a', 'z')


# for reference

# def toBinary(n):
#     return ''.join(str(1 & int(n) >> i) for i in range(64)[::-1])

# print(toBinary(10))