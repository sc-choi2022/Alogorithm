import sys

# 멜로디에 포함되어 있는 음의 수 N, 한 줄에 잇는 프렛의 수 P
N, P = map(int, sys.stdin.readline().split())
# 최소 손가락 움직임 answer
answer = 0

finger = [[] for _ in range(6+1)]

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())

    if not finger[a]:
        finger[a].append(b)
        answer += 1
    else:
        if finger[a][-1] < b:
            finger[a].append(b)
            answer += 1
        else:
            while True:
                if not finger[a] or finger[a][-1] < b:
                    finger[a].append(b)
                    answer += 1
                    break
                elif finger[a][-1] == b:
                    break
                finger[a].pop()
                answer += 1
# 멜로디를 연주하는데 필요한 최소 손가락 움직임을 출력
print(answer)