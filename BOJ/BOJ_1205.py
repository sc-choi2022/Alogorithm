import sys

# 리스트에 있는 점수의 개수 N, 태수의 새로운 점수 M, 랭킹 리스트에 올라 갈 수 있는 점수의 개수 P
N, M, P = map(int, sys.stdin.readline().split())

if N == 0:
    print(1)
else:
    # 랭킹 리스트 numbers
    numbers = list(map(int, sys.stdin.readline().split()))
    # 태수의 점수 M을 추가한 랭킹리스트
    numbers.append(M)
    numbers.sort(reverse=True)
    idx = numbers.index(M) + 1
    # 랭킹 리스트에 올라갈 수 없는 경우
    if idx > P:
        print(-1)
    else:
        # 랭킹 리스트가 꽉 차있고 새 점수가 이전 점수보다 좋지 못한 경우
        if N == P and numbers[-1] == M:
            print(-1)
        # idx 출력
        else:
            print(idx)