N, M = map(int, input().split()) #N : 입력값의 개수, M : 요청한 길이
len = list(map(int, input().split())) #입력값들을 배열에 저장
start = 0 #탐색을 시작할 지점
end = max(len) # 탐색 최대 범위
result = 0 # 찾고자하는 위치
while(start <= end):
    total = 0 # 분할로 생긴 덩어리의 합
    mid = (start + end) // 2 # 이진 탐색을 위한 중간 지점 설정
    for ary in len: #덩어리 커팅
        if  ary > mid :
            total += ary - mid
    if total < M : # 원하는 수치보다 작으면 범위를 조절(이미 탐색에 사용된 범위는 다음 탐색에서 제외시키기 위함)
        end = mid - 1
    else: #원하는 수치 이상의 값을 발견 - 겹치지 않는 범위를 좁혀가며 탐색한 결과 - 최적의 값을 도출.
        result = mid
        start = mid + 1
    
print(result)

