x = int(input())
list = []
for i in range(x):
    # y = input()
    # list.append(y)
    list.append(int(input()))

list.sort(reverse=True)    
result = ' '.join(map(str, list))
print(result)

# list = sorted(list, reverse=True)
# for i in range(len(list)):
#     print(i, end=' ')