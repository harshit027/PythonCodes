n = lambda x: x**2
print(n(2))

for i in range(1,50):
    n = lambda x: x%3 == 0
    if(n(i) != 0):
        print(i)


words = ['this', 'is', 'a', 'lamba', 'function']
lengths = list(map(lambda x: len(x), words))
print(lengths)
