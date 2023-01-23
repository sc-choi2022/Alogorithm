import sys

# 용액의 개수 N
N = int(sys.stdin.readline())
# 용액의 종류 liquid
liquid = list(map(int, sys.stdin.readline().split()))
left, right = 0, N - 1

# 0에 가까운 용액의 합을 저장할 변수 minValue
minValue = 2e+9 + 1
# 출력할 두 용액
result = (0, 0)

# 두 값의 합을 구해야하므로 =가 들어가면 안된다.
while left < right:
    leftValue, rightValue = liquid[left], liquid[right]

    # 두가지 조건문에 사용하는 두 용액의 특성값 합 변수 mixture
    mixture = leftValue + rightValue

    # 절대값 mixture가 minValue보다 작다면 minValue를 갱신
    if minValue > abs(mixture):
        minValue = abs(mixture)
        # 출력할 두 용액을 오름차순으로 result에 저장
        result = (leftValue, rightValue)

    # mixture값이 양수인 경우
    if mixture > 0:
        right -= 1
    # mixture값이 음수인 경우
    else:
        left += 1
# 두 용액의 특성값의 오름차순으로 출력
print(*result)