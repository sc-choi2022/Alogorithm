import sys

# 소수여부를 확인하는 함수 prime
def prime(N):
    if N == 1:
        return False
    for i in range(2, int(N**0.5)+1):
        if not N%i:
            return False
    return True

# 기준이 되는 수 N
N = int(sys.stdin.readline())
while True:
    check = prime(N)
    # 소수인 경우
    if check:
        # 팰린드롬 여부를 확인 후 N 출력
        if str(N) == str(N)[::-1]:
            print(N)
            break
    N += 1