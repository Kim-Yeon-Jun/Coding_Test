#순차탐색 소스코드 구현
def sequential_search(n, target, array):
    for i in range(n): #원소를 1개씩 확인하며
        if array[i] == target: # 현재의 원소가 찾고자 하는 원소와 동일한 경우
            return i+1

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요 :")
input_data = input().split()
n = int(input_data[0]) # 원소의 개수
target = input_data[1] # 찾고자 하는 문자열

print("앞서 적은 원소 개수 만큼 문자열을 입력하세요. 구분은 띄어쓰기 한칸으로 합니다.")
array = input().split()

#결과 출력
print(sequential_search(n,target,array))