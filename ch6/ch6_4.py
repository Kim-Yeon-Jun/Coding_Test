n, k = map(int, input().split(' '))

first = list(map(int, input().split(' ')))
second = list(map(int, input().split(' ')))


for i in range(k):
    mini = min(first)
    maxi = max(second)
    minl = first.index(mini)
    maxl = second.index(maxi)
    
    if mini < maxi:
        first[minl], second[maxl] = second[maxl], first[minl]
    elif mini >= maxi:
        continue

print(sum(first))

#교재 해설
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # 배열을 오름차순으로 정렬
b.sort(reverse = True) # 배열을 내림차순으로 정렬

#첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    #A의 원소가 B의 원소보다 작은 경우(두 원소를 바꿔야 하는 경우)
    if a[i] < b[i]:
        a[i],b[i] = b[i], a[i]
    else: #A의 원소가 B의 원소보다 크거나 같을 때(굳이 바꿀 이유가 없는 경우)
        break
    
print(sum(a))

#풀이 비교 : sort()를 통해 미리 정렬하고 접근하는 것과 정렬되지 않은 무작위의 데이터에 접근하는 것은
# 시간상으로 차이가 발생. 코드 구현 난이도 또한 다르기 때문에 
# 크기비교에 관해서는 데이터의 정렬에 대해서 우선적으로 생각해볼 필요가 있음