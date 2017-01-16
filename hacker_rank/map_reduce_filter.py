from functools import reduce
nums = [2,5,1,9,10,11]

l1 = list(map(lambda x: x+1, nums))
print(l1)

l2 = list(filter(lambda x: x%2 == 0, nums))
print(l2)

l3 = int(reduce(lambda x,y: x+y, nums))
print(l3)

