import sys

def solve():
    for n1 in prime:
        for n2 in prime:
            for n3 in prime:
                if n1+n2+n3 == K:
                    print(n1, n2, n3)
                    return

# 테스트케이스 수 T
T = int(sys.stdin.readline())
# 소수를 저장하는 배열 prime
prime = []
# 소수여부를 저장하는 배열 check
check = [1] * 1001

for i in range(2, 1001):
    if check[i]:
        prime.append(i)
    for j in range(i, 1001, i):
        check[j] = 0

for _ in range(T):
    # 정수 K
    K = int(sys.stdin.readline())
    solve()