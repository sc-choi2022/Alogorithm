import sys

# 소수를 저장하는 배열 prime
prime_numbers = []
# 소수의 확인여부를 저장하는 배열 check
check = [0] * 1000001
check[0], check[1] = 1, 1
# 소수를 구하는 for문
for i in range(2, 1000001):
    if not check[i]:
        prime_numbers.append(i)
        for j in range(2*i, 1000001, i):
            check[j] = 1

# 테스트 케이스의 개수 T
T = int(sys.stdin.readline())
for _ in range(T):
    # 짝수인 정수 N
    N = int(sys.stdin.readline())
    # 골드바흐 파티션의 개수 cnt
    cnt = 0
    for prime in prime_numbers:
        if prime >= N:
            break
        if not check[N-prime] and prime <= N-prime:
            cnt += 1
    # 골드바흐 파티션의 수를 출력
    print(cnt)
