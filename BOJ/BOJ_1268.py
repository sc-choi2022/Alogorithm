import sys

# 학생의 수 N
N = int(sys.stdin.readline())
# 학생들의 반의 정보를 저장하는 배열 classes
classes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 한번이라도 같은 반이었던 학생의 최대 개수 cnt, 학생의 번호 number
cnt, number = 0, 0

for i in range(N):
    # i+1번 학생과 한번이라도 같은 반이었던 학생의 개수 tmp
    tmp = 0
    for j in range(N):
        for k in range(5):
            if classes[i][k] == classes[j][k]:
                tmp += 1
                break
    # cnt 값과 학생의 번호 갱신
    if tmp > cnt:
        cnt = tmp
        number = i+1

# 임시 반장으로 정해진 학생의 번호를 출력
print(number)