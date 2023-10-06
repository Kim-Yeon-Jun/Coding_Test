array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)): #0번 인덱스 원소는 이미 정렬이 되어있다고 판단하고 1번 인덱스부터 시작
    for j in range(i, 0,-1): # i부터 1까지 1씩 줄여가면서 들어갈 위치를 탐색
        if array[j] < array[j-1]:#1칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else: #자신보다 작은 값을 만나면 멈춤
            break

print(array)