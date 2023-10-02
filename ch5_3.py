n, m = map(int, input().split())
#입력 받을 그래프
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def search(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y]=1
        search(x-1,y)
        search(x+1,y)
        search(x,y-1)
        search(x,y+1)
        return True
    return False       
count = 0

for i in range(n):
    for k in range(m):
        if search(i,k) == True:
            count += 1
            
print(count)

