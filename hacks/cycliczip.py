# the cyclic zip

first = [1,2,3,4]
second = [5,6,7,8]

zipd = list(zip(first, second))

print(zipd) # [(1, 5), (2, 6), (3, 7), (4, 8)]

unzp = list(zip(*zipd))

print(unzp) # [(1, 2, 3, 4), (5, 6, 7, 8)]

third = [first, second] # [[1, 2, 3, 4], [5, 6, 7, 8]]

print( list(zip(*third))) # equivalent of zipd

print( [ list(z) for z in zip(*zipd) ]) # equivalent of third
