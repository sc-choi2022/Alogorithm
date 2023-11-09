import sys

N = int(sys.stdin.readline())
C = [int(sys.stdin.readline()) for _ in range(N)]
C.sort(reverse=True)

answer = 0
for i in range(2, N, 3):
    answer += C[i]

print(sum(C) - answer)