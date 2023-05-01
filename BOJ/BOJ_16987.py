import sys

def solve(current):
    if current == N:
        cnt = 0
        for durability, weight in eggs:
            if durability <= 0:
                cnt += 1
        return cnt

    if eggs[current][0] <= 0:
        return solve(current+1)

    for i in range(N):
        if i == current:
            continue
        if eggs[i][0] > 0:
            break
    else:
        return solve(current+1)

    answer = 0
    for j in range(N):
        if j == current or eggs[i][0] <= 0:
            continue

        eggs[j][0] -= eggs[current][1]
        eggs[current][0] -= eggs[j][1]

        answer = max(answer, solve(current+1))

        eggs[j][0] += eggs[current][1]
        eggs[current][0] += eggs[j][1]
    return answer

# 계란의 개수 N
N = int(sys.stdin.readline())
# 계란의 내구도와 무게에 대한 정보를 담을 배열 eggs
eggs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(solve(0))