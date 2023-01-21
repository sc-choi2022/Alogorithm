import sys

# 전체 용액의 수
N = int(sys.stdin.readline())
# 용액의 특성값을 담을 배열 liq, 이분탐색을 위해 정렬
liq = list(map(int, sys.stdin.readline().split()))
liq.sort()

# 시작과 마지막 위치값을 변수 start, end에 저장
start, end = 0, N - 1
# 특성값 합의 기준이 될 absNumber
absNumber = 2e+9 + 1
# 출력할 두 용액의 특성값을 저장할 ans
ans = (0, 0)

while start < end:
    left, right = liq[start], liq[end]
    # 특성값을 더한 값을 변수 add에 저장
    add = left + right

    # absNumber 및 ans의 갱신이 필요한 경우
    if abs(add) < absNumber:
        absNumber = abs(add)
        ans = (left, right)

    # 0에 가까운 용액이 될 수 있도록 start와 end의 위치를 재할당
    if add < 0:
        start += 1
    else:
        end -= 1
# 두 용액을 출력
print(*ans)