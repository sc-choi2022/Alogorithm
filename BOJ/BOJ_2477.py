# 1m2의 넓이에 자라는 참외의 개수
K = int(input())

# 모든 길이과 방향 값을 담을 리스트 total, direction
total = []
direction = []
# 가로와 세로의 길이 값을 담을 리스트 x, y
x = []
y = []
# 큰 사각형의 넓이
area = 0
# 작은 사각형의 넓이
small_area = 0
# 6개의 방향과 길이의 정보를 받을 for문
for _ in range(6):
    d, length = map(int, input().split())
    # 동, 서의 방향일 때
    if d == 1 or d == 2:
        x.append(length)
        total.append(length)
        direction.append(d)
    # 남, 북의 방향일 때
    elif d == 3 or d == 4:
        y.append(length)
        total.append(length)
        direction.append(d)

# 방향의 전체 수인 6에 대하여 주위의 반복되는 방향 값을 확인하는 for문
for j in range(6):
    if direction[j] == direction[j-2] and direction[j-1] == direction[j-3]:
        # 반복되는 방향 값을 가질 때 중아의 두 값이 빼줄 작은 사각형의 길이 값
        # 두 값을 곱하여 작은 사각형값을 구한다.
        small_area = total[j-2] * total[j-1]
# 큰 사각형 - 작은 사각형
area = max(x) * max(y) - small_area
# 1m2의 넓이에 자라는 참외의 개수를 곲하여 출력
print(area * K)