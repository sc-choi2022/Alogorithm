import sys

# 중간 지점의 개수 N
N = int(sys.stdin.readline())
# 각 중간지점의 속력 제한을 저장하는 배열 V
V = list(map(int, sys.stdin.readline().split()))
# 최대 연습의 성과 answer
answer = 1

pre = 1
for i in range(N-2, -1, -1):
    if pre < V[i]:
        pre += 1
    elif pre > V[i]:
        pre = V[i]
    answer += pre
# answer 출력
print(answer)