n = int(input())
s_name = []
s_score = []
for i in range(n):
    name, score = map(str, input().split(' '))
    s_name.append(name)
    s_score.append(int(score))

for k in range(n):
    mini = k
    for j in range(k+1, n):
        if s_score[mini] > s_score[j]:
            mini = j
    s_score[k], s_score[mini] = s_score[mini], s_score[k]
    s_name[k], s_name[mini] = s_name[mini], s_name[k]
result = ' '.join(map(str, s_name))
print(result)
#===================================================
#계수정렬을 이용한 문제풀이(해설)
n = int(input())
array = []
for i in range(n):
    input_data = input().split()
    #2차원 데이터로 저장
    array.append((input_data[0], int(input_data[1])))
    
array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')
    

#위의 방식에서는 1차원 배열 2개를 사용하였지만 아래 방식에서는 2차원배열 1개로 처리
# 이름 / 점수 배열 => (이름, 점수)