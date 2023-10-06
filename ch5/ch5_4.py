from collections import deque
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
#상하 좌우 움직임을 2개의 배열로 구성
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
#최단거리 찾기를 위한 함수 선언
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        # 큐의 제일 왼쪽 좌표를 꺼냄
        x, y = queue.popleft()
        #4개의 방향에 대해 반복문 설정
        for i in range(4):
            #상하좌우로 이동할 경우의 좌표값
            nx = x + dx[i]
            ny = y + dy[i]
            #다음 이동 좌표가 맵을 벗어난 경우
            if nx < 0 or nx > n or ny < 0 or ny > m:
                continue
            #다음 이동 좌표가 갈 수 없는 곳인 경우
            if graph[nx][ny] == 0:
                continue
            #다음 이동 좌표가 갈 수 있는 곳인 경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 #거리를 확인하기 위해 1씩 증가시키는 값을 저장
                queue.append((nx,ny))
    return graph[n-1][m-1] # 마지막 출구에 저장된 값 = 도착까지 걸린 횟수 반환

print(bfs(0,0))