import sys
sys.setrecursionlimit(10**6)

# 아래 주사위의 윗 숫자 number, 쌓은 주사위의 갯수 cnt, 더해지는 옆면의 값 add
def dfs(number, cnt, add):
    global answer

    if cnt == N:
        answer = max(answer, add)
        return
    # number와 같은 숫자의 인덱스 idx, 마주보는 위의 수의 위치 idxPair
    idx = dices[cnt].index(number)
    idxPair = pairs[idx]
    # 더해지는 옆면의 최대수 maxNumber
    maxNumber = 0
    for j in range(6):
        if j == idx or j == idxPair:
            continue
        maxNumber = max(maxNumber, dices[cnt][j])
    dfs(dices[cnt][idxPair], cnt+1, add+maxNumber)

# 마주보는 주사위의 위치를 저장하는 딕셔너리 pairs
pairs = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}

# 주사위의 개수 N
N = int(sys.stdin.readline())
# 주사위의 수들을 저장하는 배열 dices
dices = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 한 옆면의 숫자의 합이 가장 큰 값 answer
answer = 0

for i in range(6):
    pair = pairs[i]
    # 옆면의 최댓값이 6일 수 있는 경우
    if dices[0][i] != 6 and dices[0][pair] != 6:
        dfs(dices[0][i], 1, 6)
    elif dices[0][i] == 6 or dices[0][pair] == 6:
        # 옆면의 최댓값이 4일 수 있는 경우
        if dices[0][i] == 5 or dices[0][pair] == 5:
            dfs(dices[0][i], 1, 4)
        # 옆면의 최댓값이 5일 수 있는 경우
        else:
            dfs(dices[0][i], 1, 5)

# 한 옆면의 숫자의 합이 가장 큰 값 answer을 출력
print(answer)