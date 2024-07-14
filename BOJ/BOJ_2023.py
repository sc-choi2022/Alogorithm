import sys

# 소수를 확인하는 함수 prime
def prime(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

def dfs(num):
    if len(str(num)) == N:
        print(num)
        return
    for j in range(1, 10, 2):
        if prime(num * 10 + j):
            dfs(num * 10 + j)

# 소수의 자리 수 N
N = int(sys.stdin.readline())

# 한 자리수 소수로 매개변수로 dfs 실행
for p in (2, 3, 5, 7):
    dfs(p)