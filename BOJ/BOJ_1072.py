import sys

# 게임 횟수 X, 이긴 게임 횟수 Y
X, Y = map(int, sys.stdin.readline().split())
# 현재 형택이의 승률 Z
Z = 100 * Y // X
# 필요한 추가 게임 횟수 ans
ans = -1

# 추가 게임 횟수를 구하는 이분탐색의 초기 값 start, end
start, end = 1, 1000000000

while start <= end:
    mid = (start + end) // 2
    # mid번으로 변경되는 게임 횟수 tx, 이긴 게임 횟수 ty
    tx, ty = X + mid, Y + mid
    # tx, ty에 따른 승률 tz
    tz = 100 * ty // tx

    # Z와 tz의 값이 다른 경우 end를 조절 후 ans값을 갱신
    if Z != tz:
        end = mid - 1
        ans = mid
    # Z와 tz의 값이 같은 경우
    else:
        start = mid + 1
# 승률이 변하기 위한 최소 승리횟수 출력
print(ans)