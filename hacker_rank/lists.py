L = []
n = int(input())
for i in range(n):
    cmd = input().split(" ")
    if (cmd[0] == 'insert'):
        L.insert(int(cmd[1]), int(cmd[2]))
    elif (cmd[0] == 'print'):
        print(L)
    elif (cmd[0] == 'remove'):
        index = L.index(int(cmd[1]))
        del L[index]
    elif (cmd[0] == 'append'):
        L.append(int(cmd[1]))
    elif (cmd[0] == 'sort'):
        L.sort()
    elif (cmd[0] == 'pop'):
        L.pop()
    elif (cmd[0] == 'reverse'):
        L.reverse()

