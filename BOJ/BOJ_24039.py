import sys

# 주어지는 수 N
N = int(sys.stdin.readline())
# 소수의 내용을 저장하는 배열 prime
prime = [1 for _ in range(N+1)]
# 특별한 수를 저장하는 배열 special
special = []
start = 0

# 특별한 수가 6인 경우
if N < 4:
    print(6)
else:
    for i in range(1, int(N**0.5)+1):
        j = 2
        while i*j <= N:
            prime[i*j] = 0
            j += 1
    for ii in range(2, N+1):
        if prime[ii]:
            special_number.append(ii)
            if ii <= int(N**0.5):
                start = ii

    for iii in range(prime_number.index(start), len(special_number)-1):
        result = special_number[iii]*special_number[iii+1]
        if result > N:
            print(result)
            break