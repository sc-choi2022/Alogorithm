import sys

N = int(sys.stdin.readline())
prime = [1 for _ in range(N+1)]
prime_number = []
start = 0

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
            prime_number.append(ii)
            if ii <= int(N**0.5):
                start = ii

    for iii in range(prime_number.index(start), len(prime_number)-1):
        result = prime_number[iii]*prime_number[iii+1]
        if result > N:
            print(result)
            break