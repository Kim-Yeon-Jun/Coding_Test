N, M = map(int, input().split())

array = []
#화폐의 단위를 입력받음
for i in range(N):
    array.append(int(input()))
    
# 해당되지 않는 값에 대한 구분을 위해 -1로 초기화    
d = [-1] * ( M + 1 )
# 0을 만들기 위해 필요한건 0개
d[0] = 0
#화폐 단위 N개 마다 반복문으로 필요한 화폐의 개수 업데이트
for i in range(N):
    for j in range(array[i], M+1):
        # 현재 화폐의 단위로 표현이 가능한 경우 업데이트
        if (d[j - array[i]] != -1):
            d[j] = min(d[j], d[j-array[i]]+1)
            
if d[M] == -1:
    print(-1)
else:
    print(d[M])