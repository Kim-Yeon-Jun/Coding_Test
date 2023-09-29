line = input()
x_list = []
y_list = []
n = len(line)
for i in range(n):
    a, b, c = line[i]
    for k in range(i+1,n):
        d, e, f = line[k][0:3]
        if a * d == b * c :
            continue
        x = (b*f-e*d)/(a*d-b*c)
        y = (e*c-a*f)/(a*d-b*c)
        if type(x) != type(1) | type(y) != type(1):
            continue
        x_list.append(x)
        y_list.append(y)

min_x = min(x_list)
max_x = max(x_list)
min_y = min(y_list)
max_y = max(y_list)

size_x = max_x - min_x
size_y = max_y - min_y

empty_loc = [['.']*size_x]*size_y

print(empty_loc)
