import sys

def dfs(sequence):
    # 길이 M의 수열이 완성된 경우 print
    if len(sequence) == M:
        print(*sequence)
        return

    for i in range(N):
        # 자연수 i+1을 sequence에 추가할 수 있는 경우
        if not visit[i]:
            sequence.append(i+1)
            visit[i] = 1
            dfs(sequence)
            sequence.pop()
            visit[i] = 0


# 1부터 N까지 자연수의 기준 N, 만드는 수열의 길이 M
N, M = map(int, sys.stdin.readline().split())
# 수열에 선택한 자연수를 확인하기 위한 배열 visit
visit = [0] * N
# 수열을 만드는 함수 dfs
dfs([])