import sys

# 이번 학기의 분 수 N
N = int(sys.stdin.readline())
# 마치지 못한 과제를 저장하는 배열
HW = []
# 받게 되는 과제 점수 score
score = 0
for _ in range(N):
    # 과제의 정보를 저장하는 배열 info
    info = list(map(int, sys.stdin.readline().split()))

    # 과제가 주어진 경우
    if info[0]:
        info[2] -= 1
        if info[2]:
            HW.append((info[1], info[2]))
        else:
            score += info[1]
    else:
        if HW:
            tmp = HW.pop()
            if tmp[1] - 1:
                HW.append((tmp[0], tmp[1]-1))
            else:
                score += tmp[0]
# 받을 과제 점수를 출력
print(score)