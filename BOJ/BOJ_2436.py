import sys

# 서로소를 찾는 함수 find
def find(a, b):
    while b > 0:
        print(a, b)
        a, b = b, a%b
    print(f'return {a}')
    return a

# 최대공약수와 최소공배수로 하는 두 개의 자연수 A, B(A<B)
A, B = map(int, sys.stdin.readline().split())
# B // A를 저장하는 변수 C
C = B // A

for i in range(int(C**0.5), 0, -1):
    if C%i == 0 and find(i, C//i) == 1:
        print(A*i, A*C//i)
        break