n = int(input()) # 창고의 갯수
x = list(map(int, input().split())) # 창고에 저장된 식량의 갯수

#계산된 결과를 저장하기 위한 배열 선언
#계산 과정을 범위를 잡아가면서 하면 편함
#입력 요소가 10개면 - 1개일때 / 2개일때 / /...
d = [0]*100

d[0] = x[0]
d[1] = max(x[0], x[1])

for i in range(2, n):
    d[i] = max(d[i-2]+x[i], d[i-1])

print(d[n-1])
