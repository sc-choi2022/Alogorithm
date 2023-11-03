import sys

def guess(N):
    for k in range(3, N, 2):
        if numbers[k] and numbers[N-k]:
            print(f'{N} = {k} + {N-k}')
            return
    print("Goldbach's conjecture is wrong.")
    return
# 소수여부를 저장하는 배열 numbers
numbers = [1]*1000001
for i in range(2, int(1000001**0.5)+1):
    if numbers[i]:
        for j in range(2*i, 1000001, i):
            numbers[j] = 0

while True:
    # 정수 N
    N = int(sys.stdin.readline())

    if N == 0:
        break
    guess(N)