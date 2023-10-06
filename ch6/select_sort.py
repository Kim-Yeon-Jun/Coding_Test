array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i #최솟값(탐색)의 인덱스
    for j in range(i+1, len(array)):#맨앞을 제외한 범위에서
        if array[min_index] > array[j]: #맨앞의 값보다 작은 값이 발견되면
            min_index = j #최솟값을 가리키는 인덱스 업데이트
    array[i], array[min_index] = array[min_index], array[i] #1번의 탐색과정이 끝나면(한 범위내에서 최솟값을 찾는 과정이 끝나면) 
                                                            #최솟값의 위치와 다음번에 범위에서 빠질 위치의 값을 swap

print(array)