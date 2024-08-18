import sys

def dfs(equation, result):
    global answer, cnt
    # K번째 식이 구해진 경우
    if answer != '-1':
        return
    # 식이 완성된 경우 cnt 1 증가
    if result == N:
        cnt += 1
        # K번째 식인 경우 answer에 저장
        if cnt == K:
            answer = equation
        return

    for j in (1, 2, 3):
        if result + j <= N:
            dfs(equation+'+'+str(j), result+j)


# 합으로 구하는 정수 N, 구해야하는 순번 K
N, K = map(int, sys.stdin.readline().split())
# K번째 식을 저장하는 변수 answer, 만들어진 식의 개수 cnt
answer, cnt = '-1', 0

for i in (1, 2, 3):
    dfs(str(i), i)
# answer을 출력
print(answer)