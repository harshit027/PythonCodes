n = input()
L = [int(x) for x in input().split()]
L.sort()
n = L.pop()
while True:
    m = L.pop()
    if m != n:
        print(m)
        break
