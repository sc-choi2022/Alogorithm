from collections import defaultdict
import sys

# 참여하는 사람 수 N
N = int(sys.stdin.readline())
# 가장 큰 상금을 저장하는 변수 money
money = 0

for _ in range(N):
    # 주사위 결과를 저장한 딕셔너리 dice
    dice = defaultdict(int)
    # 사람들이 던지 4개의 눈의 결과 result
    result = list(map(int, sys.stdin.readline().split()))
    for i in range(4):
        dice[result[i]] += 1
    # dice의 배열 lst
    lst = sorted(list(dice.items()), key=lambda x:(-x[1], -x[0]))
    if len(lst) == 1:
        money = max(money, 50000+lst[0][0]*5000)
    elif len(lst) == 2:
        if lst[0][1] == 3:
            money = max(money, 10000+lst[0][0]*1000)
        else:
            money = max(money, 2000+(lst[0][0]+lst[1][0])*500)
    elif len(lst) == 3:
        money = max(money, 1000+lst[0][0]*100)
    else:
        money = max(money, lst[0][0]*100)
# money 출력
print(money)