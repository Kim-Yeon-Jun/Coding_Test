N = int(input())
list_N = list(map(int, input().split()))
M = int(input())
list_M = list(map(int, input().split()))

result = ['no' for i in range(M)]

for i in range(M):
    for j in range(N):
        if list_M[i] in list_N:
            result[i]='yes'

result = ' '.join(map(str, result))
print(result)


# 내 풀이 : 결과 값 출력을 위한 배열 생성(no로 초기화)
# 이중 반복분을 통해 찾고자 하는 값이 있으면 
# 배열의 값을 yes로 초기화 후 출력

# 이진 탐색 : 
# 입력받은 배열을 정렬 시킨후
# 이진 탐색으로 값을 찾음
# 찾은 결과 : None(없음)이면 no, 있으면(!=None) yes 출력

# 계수정렬 : 적당한 크기의 1차원 배열을 0으로 초기화 생성
# 들어온 값을 인덱스로 취급. 해당 인덱스의 배열값을 1로 변경
# 찾고자 하는 값을 받고 이 또한 인덱스로 취급하여 
# 같은 배열에서 인덱스로 접근하여 찾음

# 집합 자료형 set :
# 들어온 값을 set(map(int, input().split())) : 집합으로 처리
# 단순 반복문과 조건문(if i in array)으로 있는지 확인하고
# yes or no 출력