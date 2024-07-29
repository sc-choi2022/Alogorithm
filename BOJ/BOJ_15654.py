import sys

def dfs(sequence):
    # 길이 M의 수열이 완성된 경우 print
    if len(sequence) == M:
        print(*sequence)
        return

    for i in range(N):
        # numbers[i]을 sequence에 추가할 수 있는 경우
        if not visit[i]:
            sequence.append(numbers[i])
            visit[i] = 1
            dfs(sequence)
            sequence.pop()
            visit[i] = 0

# 1부터 N까지 자연수의 기준 N, 만드는 수열의 길이 M
N, M = map(int, sys.stdin.readline().split())
# 주어지는 N개의 자연수를 정렬하여 저장하는 numbers
numbers = sorted(map(int, sys.stdin.readline().split()))
visit = [0] * N
# 수열을 만드는 함수 dfs
dfs([])