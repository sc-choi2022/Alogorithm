import sys

def dfs(sequence):
    # 길이 M의 수열이 완성된 경우 print
    if len(sequence) == M:
        print(*sequence)
        return

    for i in range(N):
        if not sequence or (sequence and sequence[-1] <= i+1):
            sequence.append(i+1)
            dfs(sequence)
            sequence.pop()

# 1부터 N까지 자연수의 기준 N, 만드는 수열의 길이 M
N, M = map(int, sys.stdin.readline().split())
# 수열을 만드는 함수 dfs
dfs([])