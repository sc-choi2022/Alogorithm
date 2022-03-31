import sys
sys.stdin = open('sample_input.txt')

# 테스트케이스의 개수
test_case = int(input())
for case in range(1, test_case+1):
    # 집합의 원소의 개수 N, 부분집합의 합 기준 S
    N, S = map(int,input().split())
    # 집합의 N개의 원소를 담을 sets
    sets = list(map(int, input().split()))
    # 부분집합의 개수를 세는 cnt 값 초기화
    cnt = 0

    # 비트 연산자를 활용하여 부분집합 생성
    for i in range(1<<N):
        # 부분 집합의 초기 공집합
        subset = []
        for j in range(N):
            if i&(1<<j):
                subset.append(sets[j])
        # S값과 비교하기 위한 subset의 부분집합 합 compare를 초기화
        compare = 0
        # compare 값을 구하는 for문
        for sub in subset:
            compare += sub
        # compare값이 목표하는 S와 같다면
        if compare == S:
            # cnt에 1을 더한다.
            cnt += 1
    # 부분집합의 합이 S인 부분집합의 개수 출력
    print(f'{cnt}')

def dfs(n, arr):
    global cnt
    # 완성 전에 합이 S를 넘으면
    if sum(arr) > S:
        return
    # 부분집합 완성
    if n == N:
        # 합이 S면 cnt 1증가
        if sum(arr) == S:
            cnt += 1
        return

    dfs(n+1, arr + [lst[n]])    # lst[n]을 포함
    dfs(n+1, arr)               # lst[n]을 미포함

T = int(input())
for case in range(1, T + 1):
    # 집합의 원소의 수 N, 합이 기준 S
    N, S = map(int, input().split())
    # N개의 원소를 가진 집합 리스트 lst
    lst = list(map(int, input().split()))
    # 부분집합의 합이 S인 개수 cnt 초기화
    cnt = 0
    # lst의 0 인덱스와 빈 리스트로 시작
    dfs(0, [])
    # cnt 출력
    print(cnt)