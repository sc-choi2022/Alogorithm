import sys

def dfs(sequence):
    # 길이 M의 수열이 완성된 경우 print
    if len(sequence) == M:
        print(*sequence)
        return

    # 수열의 현재 위치의 자연수 확인을 위한 변수 check
    check = 0
    for i in range(N):
        # 주어지는 N개의 자연수의 중복을 고려
        if not visit[i] and check != numbers[i]:
            sequence.append(numbers[i])
            visit[i] = 1
            check = numbers[i]
            dfs(sequence)
            sequence.pop()
            visit[i] = 0

# 1부터 N까지 자연수의 기준 N, 만드는 수열의 길이 M
N, M = map(int, sys.stdin.readline().split())
# 주어지는 N개의 자연수를 정렬하여 저장하는 numbers
numbers = sorted(map(int, sys.stdin.readline().split()))
# 수열에 사용여부를 저장하는 배열 visit
visit = [0] * N
# 수열을 만드는 함수 dfs
dfs([])