import sys

N, M = map(int, sys.stdin.readline().split())
li = sorted([int(sys.stdin.readline()) for _ in range(M)])
MaxP, MaxB = 0, 0

for i in range(M):
    t = li[i] * ((M - i) if M - i <= N else N)
    if MaxB < t:
        MaxB = t
        MaxP = li[i]
print(MaxP, MaxB)