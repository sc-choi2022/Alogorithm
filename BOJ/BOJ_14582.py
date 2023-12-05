import sys

# 울림 제미니스의 득점을 저장하는 배열 team1
team1 = list(map(int, sys.stdin.readline().split()))
# 스타트링크 걸리버스의 득점을 저장하는 배열 team2
team2 = list(map(int, sys.stdin.readline().split()))
# 울림 제미니스의 득점이 더 높은 회차가 있었는지 여부를 저장하는 변수 flag
flag = False
# 울림 제미니스의 득점 score1, 스타트링크의 득점 score2
score1, score2 = 0, 0
for i in range(9):
    # i회 초 점수를 추가
    score1 += team1[i]
    # 울림 제미니스가 이긴 시점이 있는 경우
    if score1 > score2:
        flag = True
        break
    # i회 후 점수를 추가
    score2 += team2[i]

# 울림 제미니스가 역전패를 했다면 'Yes'를 그렇지 않으면 'No'를 출력
print('Yes' if flag else 'No')