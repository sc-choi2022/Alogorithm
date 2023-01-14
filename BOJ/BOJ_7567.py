import sys

# 그릇의 방향이 주어진다.
bowl = sys.stdin.readline().rstrip()

# 비교할 이전 그릇의 모양을 변수 pre에 저장
pre = bowl[0]
# 주어진 그릇의 개수 N
N = len(bowl)

# 출력할 높이 height의 값을 맨 처음 그릇의 높이 10으로 초기화
height = 10

for i in range(1, N):
    # 그릇이 같은 방향인 경우
    if pre == bowl[i]:
        height += 5
    # 그릇이 다른 방향인 경우
    else:
        height += 10
    # 그릇의 위치를 재설정
    pre = bowl[i]

# 높이를 출력
print(height)