import sys

# 다친 손가락의 번호 1 엄지 2 검지 3 중지 4 약지 5 새끼
injured = int(sys.stdin.readline())
# 다친 손가락이 셀 수있는 횟수
repeat = int(sys.stdin.readline())
# 세는 기준이 되는 injured - 1의 값을 변수 base에 저장
base = injured - 1

# 엄지 혹은 새끼 손가락을 다친 경우
if injured == 1 or injured == 5:
    print(base + 8 * repeat)
# 중지 손가락을 다친 경우
elif injured == 3:
    print(base + 4 * repeat)
# 검지 손가락을 다친 경우
elif injured == 2:
    # 반복 횟수가 홀수인 경우
    if repeat % 2:
        print(base + 8 * (repeat // 2) + 6)
    # 반복 횟수가 짝수인 경우
    else:
        print(base + 8 * (repeat // 2))
# 약지 손가락을 다친 경우
elif injured == 4:
    # 반복 횟수가 홀수인 경우
    if repeat % 2:
        print(base + 8 * (repeat // 2) + 2)
    # 반복 횟수가 짝수인 경우
    else:
        print(base + 8 * (repeat // 2))