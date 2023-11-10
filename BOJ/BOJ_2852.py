import sys

# 골이 들어간 횟수 N
N = int(sys.stdin.readline())
# 팀 1, 2가 이긴 횟수를 저장하는 변수 win1, win2 각 팀의 이긴 시간 time1, time2
win1, win2, time1, time2 = 0, 0, 0, 0

tmp = 0
for _ in range(N):
    # 팀 번호 team, 득점시간 time
    team, time = sys.stdin.readline().rstrip().split()
    # 득점시간 MM, SS
    MM, SS = map(int, time.split(':'))

    if win1 > win2:
        time1 += (MM*60 + SS) - tmp
    elif win2 < win2:
        time2 += (MM*60 + SS) - tmp
        
TMM1, TSS1, TMM2, TSS2 = str(time1//60), str(time1%60), str(time2//60), str(time2%60)
print(f'{TMM1 if len(TMM1) == 2 else "0"+TSS1}:{TSS1 if len(TSS1) == 2 else "0"+TSS1}')
print(f'{TMM1 if len(TMM2) == 2 else "0"+TSS2}:{TSS2 if len(TSS2) == 2 else "0"+TSS2}')