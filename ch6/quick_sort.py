array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end: # 배열의 원소가 1개인 경우 종료(재귀함수 종료조건)
        return
    pivot = start # 첫번째원소를 피벗으로 지정
    left = start+1
    right = end
    while left <= right:
        #지정된 범위내에서 피벗보다 큰 데이터가 발견될 때 까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        #지정된 범위내에서 피벗보다 작은 데이터가 발견될 때 까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1 
        #중간에서 엇갈렸다면 작은데이터와 피벗을 swap
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else: #엇갈리지 않았다면 작은 데이터와 큰 데이터를 swap
            array[left], array[right] = array[right], array[left]
    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행 (재귀함수 호출)
    quick_sort(array, start, right-1)
    quick_sort(array, right + 1, end)
    
quick_sort(array, 0, len(array)-1)
print(array)