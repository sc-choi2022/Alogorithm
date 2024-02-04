import sys

# 원소가 어떤 집합에 속해있는 지 확인하는 함수 find
def find(N):
    if parents[N] != N:
        parents[N] = find(parents[N])
    return parents[N]

# 서로 다른 두 개의 집합을 하나의 집합으로 병합하는 연산 함수 union
def union(a, b):
    a, b = find(a), find(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

# 입력의 끝에 도달할 때까지 반복하는 while
while True:
    # 집의 수 M, 길의 수 N
    M, N = map(int, sys.stdin.readline().split())

    if not M and not N:
        break
    # 집의 상위 집을 저장하는 배열 parents
    parents = [i for i in range(M+1)]
    # 집을 연결하는 길의 정보를 저장하는 배열 edges
    edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    edges.sort(key=lambda x:x[2])
    # 가로등을 꺼 절약하는 비용 answer
    answer = 0

    for a, b, c in edges:
        if find(a) != find(b):
            union(a, b)
        else:
            answer += c
    # 절약할 수 있는 최대 비용을 출력
    print(answer)