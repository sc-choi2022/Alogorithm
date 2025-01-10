import sys

# 이동하려고 하는 채널 N
N = int(sys.stdin.readline().rstrip())
# 고장난 버튼의 개수 M
M = int(sys.stdin.readline())
broken = list(map(int, sys.stdin.readline().split()))

answer = abs(100-N)

for i in range(1000001):
    i = str(i)

    for j in range(len(i)):
        if int(i[j]) in broken:
            break
        elif j == len(i)-1:
            answer = min(answer, abs(int(i)-N)+len(i))

print(answer)