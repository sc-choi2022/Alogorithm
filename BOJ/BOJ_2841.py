import sys

# 멜로디에 포함되어 있는 음의 수 N, 한 줄에 잇는 프렛의 수 P
N, P = map(int, sys.stdin.readline().split())
# 최소 손가락 움직임 answer
answer = 0
# 눌린 손가락을 저장하는 배열 finger
finger = [[] for _ in range(6+1)]

for _ in range(N):
    # 줄의 번호 a, 프렛의 번호 b
    a, b = map(int, sys.stdin.readline().split())
    # 줄을 처음 누르는 경우
    if not finger[a]:
        finger[a].append(b)
        answer += 1
    # 줄을 누른 손가락이 있는 경우
    else:
        # 한 번의 움직음으로 음을 연주할 수 있는 경우
        if finger[a][-1] < b:
            finger[a].append(b)
            answer += 1
        # 음 연주를 위해 추가 움직임이 필요한 경우
        else:
            while True:
                # 줄에 누른 손가락이 없거나 손가락을 눌러 음을 연주할 수 있는 경우
                if not finger[a] or finger[a][-1] < b:
                    finger[a].append(b)
                    answer += 1
                    break
                # 현재 누른 손가락으로 연주가 가능한 경우
                elif finger[a][-1] == b:
                    break
                finger[a].pop()
                answer += 1

# 멜로디를 연주하는데 필요한 최소 손가락 움직임을 출력
print(answer)