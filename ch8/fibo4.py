#피보나치 수열 보텀업 방식
d = [0] * 100

d[1] = 1
d[2] = 2
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])