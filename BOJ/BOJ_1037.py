# 약수의 개수 N
N = int(input())

# 모든 약수들이 담긴 리스트
divisor = list(map(int,input().split()))

if N == 1:
    print(divisor[0]*divisor[0])
else:
    print(min(divisor)*max(divisor))