#메모이제이션을 위한 리스트
d = [0]*100

#피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    #case1 종료조건
    if x == 1 or x == 2:
        return 1
    #case2 이미 계산한적 있는 값
    if d[x] != 0:
        return d[x]
    #case3 처음 계산하는 값
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))