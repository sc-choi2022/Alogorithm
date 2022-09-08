import sys

def func(A, B, C):
    # B값이 1이라면 A%C을 return
    if B == 1:
        return A%C
    else:
        # A^(B//2)%C을 구하기 위해 func(A, B//2, C)을 실행
        k = func(A, B//2, C)
        # B//2에 나머지가 없었다면 A^(B//2)%C의 제곱을 C로 나눈 나머지를 return
        if B%2==0:
            return k*k%C
        else:
        # B//2에 나머지가 없었다면 A^(B//2)%C의 제곱에 A을 곱한 값을 C로 나눈 나머지를 return
            return k*k*A%C


# 자연수 A, B, C
A, B, C = map(int, sys.stdin.readline().split())
print(func(A,B,C))