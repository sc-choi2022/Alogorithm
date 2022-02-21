import sys
sys.stdin = open('sample_input.txt')

test_case = int(input())
for case in range(1, test_case+1):
    N, S = map(int,input().split())
    sets = list(map(int, input().split()))
    cnt = 0

    for i in range(1<<N):
        subset = []
        for j in range(N):
            if i&(1<<j):
                subset.append(sets[j])
        compare = 0
        for sub in subset:
            compare += sub
        if compare == S:
            cnt += 1
            print(cnt)
    print(f'{cnt}')