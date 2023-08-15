import sys

# 4개의 톱니바퀴를 저장하는 배열 gear
gear = [list(sys.stdin.readline().rstrip()) for _ in range(4)]
# 해당 톱니바퀴의 회전여부와 방향을 저장하는 배열 flag
flag = [[False, 0] for _ in range(4)]

# 회전 횟수 K
K = int(sys.stdin.readline())
for _ in range(K):
    # 회전시킨 톱니바퀴의 번호 number, 방향 direction
    number, direction = map(int, sys.stdin.readline().split())
    # 지정된 톱니바퀴의 회전정보 갱신
    flag[number-1] = [True, direction]
    # 회전의 방향을 저장하는 변수 tmp
    tmp = direction
    for i in range(number-1, 0, -1):
        # i-1번째 톱니바퀴에 회전이 필요한 경우
        if gear[i][6] != gear[i-1][2]:
            # 톱니바퀴의 회전정보 갱신 후 회전 방향 변경
            flag[i-1] = [True, -tmp]
            tmp *= -1
        else:
            break
    # 회전의 방향을 direction으로 초기화
    tmp = direction
    for j in range(number-1, 3):
        # j+1번째 톱니바퀴에 회전이 필요한 경우
        if gear[j][2] != gear[j+1][6]:
            flag[j+1] = [True, -tmp]
            tmp *= -1
        else:
            break
    for k in range(4):
        # k번째 톱니바퀴의 회전여부 G, 회전방향 D
        G, D = flag[k]
        if G:
            # 시계방향
            if D == 1:
                gear[k] = gear[k][-1:] + gear[k][:7]
            # 시계반대방향
            else:
                gear[k] = gear[k][1:] + gear[k][:1]
    # 회전정보를 초기화
    flag = [[False, 0] for _ in range(4)]

# 네 톱니바퀴의 점수를 저장하는 배열 score
score = [1, 2, 4, 8]
# K번 회전시킨 이후에 네 톱니바퀴의 점수의 합 answer
answer = 0

for l in range(4):
    # 톱니바퀴의 12시방향이 S극인 경우
    if gear[l][0] == '1':
        answer += score[l]
# K번 회전시킨 이후에 네 톱니바퀴의 점수의 합을 출력
print(answer)