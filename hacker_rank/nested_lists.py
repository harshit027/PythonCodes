from operator import itemgetter

input_list = [['Sona',-25.001],['Mona',-25.0001],['Mini',-25.000],['Rita',-25.0]]

l = sorted(input_list, key = itemgetter(1))
l.reverse()
s0 = l.pop()
lowest = s0[1]
second_lowest = -100
l.reverse();
for i in range(len(l)):
    if(l[i][1]>lowest):
        second_lowest = l[i][1]
        break

output_list = list(filter(lambda x: x[1] == second_lowest, l))
print(output_list)

sorted_output_list = sorted(output_list, key = itemgetter(0))
for i in range(len(sorted_output_list)):
    print(sorted_output_list[i][0])