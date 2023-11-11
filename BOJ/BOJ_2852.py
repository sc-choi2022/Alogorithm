import sys

# 골이 들어간 횟수 N
N = int(sys.stdin.readline())
# 이전 경기에 대한 정보를 저장하는 배열 pre [이기고 있는 팀/ 마지막 골 시간]
pre = [0, 0]
# 팀1과 팀2의 현재 골 수와 이긴 시간을 저장하는 배열 team1, team2
team1, team2 = [0, 0], [0, 0]

for _ in range(N):
    # 골을 넣은 팀 team, 시간 time
    team, time = sys.stdin.readline().split()
    # 득점시간 분 MM, 초 SS
    MM, SS = map(int, time.split(':'))
    MMSS = 60 * MM + SS
    # 동점이었던 경우
    if pre[0] == 0:
        if team == '1':
            team1[0] += 1
            pre = [1, MMSS]
        else:
            team2[0] += 1
            pre = [2, MMSS]
    # 이기고 있는 팀이 팀1인 경우
    elif pre[0] == 1:
        if team == '1':
            team1[0] += 1
            team1[1] += MMSS - pre[1]
            pre[1] = MMSS
        # 팀2가 골을 넣은 경우
        else:
            # 여전히 팀1이 이기는 경우
            if team1[0] > team2[0] + 1:
                team1[1] += MMSS - pre[1]
                pre = [1, MMSS]
            # 동점이 되는 경우
            elif team1[0] == team2[0] + 1:
                team1[1] += MMSS - pre[1]
                pre = [0, MMSS]
            team2[0] += 1
    # 이기고 있는 팀이 팀2인 경우
    else:
        if team == '2':
            team2[0] += 1
            team2[1] += MMSS - pre[1]
            pre[1] = MMSS
        # 팀1이 골을 넣은 경우
        else:
            # 여전히 팀2가 이기는 경우
            if team1[0] + 1 < team2[0]:
                team2[1] += MMSS - pre[1]
                pre = [2, MMSS]
            # 동점이 되는 경우
            elif team1[0] + 1 == team2[0]:
                team2[1] += MMSS - pre[1]
                pre = [0, MMSS]
            team1[0] += 1

# 팀 1이 이기고 있는 경우
if pre[0] == 1:
    team1[1] += 48*60 - MMSS
# 팀 2이 이기고 있는 경우
elif pre[0] == 2:
    team2[1] += 48*60 - MMSS

# 첫째 줄에 1번 팀이 이기고 있던 시간, 둘째 줄에 2번 팀이 이기고 있던 시간을 출력
MM1, SS1, MM2, SS2 = str(team1[1]//60), str(team1[1]%60), str(team2[1]//60), str(team2[1]%60)
print(f'{MM1 if len(MM1) == 2 else "0"+MM1}:{SS1 if len(SS1) == 2 else "0"+SS1}')
print(f'{MM2 if len(MM2) == 2 else "0"+MM2}:{SS2 if len(SS2) == 2 else "0"+SS2}')