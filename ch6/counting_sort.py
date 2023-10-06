#모든 원소의 값이 0보다 크거나 같다고 가정
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
#모든 범위를 포함하는 크기의 배열 생성 및 0으로 초기화
count = [0]* (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값을 카운트

for i in range(len(count)): # 리스트에 저장된 정보 확인
    for j in range(count[i]): # 값들을 횟수 만큼 출력
        print(i, end=' ')