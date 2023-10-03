import sys

# 사람의 수 N
N = int(sys.stdin.readline())
# 자신보다 키가 큰 사람이 왼쪽에 몇명 있었는지 저장하는 배열 taller
taller = list(map(int, sys.stdin.readline().split()))
# 줄을 선 순서대로 저장하는 배열 align
align = [0]*N

for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == taller[i] and not align[j]:
            align[j] = i+1
            break
        elif not align[j]:
            cnt += 1
# 줄을 선 순서대로 키를 출력
print(*align)