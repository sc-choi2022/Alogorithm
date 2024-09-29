from collections import defaultdict
import sys

# 땅의 크기 N, 나무의 그루수 M, 지나는 해 K년
N, M, K = map(int, sys.stdin.readline().split())
# 겨울에 추가 되는 양분의 정보를 저장하는 배열 A
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 땅의 양분을 저장하는 배열 land
land = [[5]*N for _ in range(N)]
# 묘목의 정보를 저장하는 딕셔너리 trees
trees = defaultdict(list)

for _ in range(M):
    # 나무의 위치 x, y, 나무의 나이 z
    x, y, z = map(int, sys.stdin.readline().split())
    trees[(x-1, y-1)].append(z)

for _ in range(K):
    next = defaultdict(list)
    for location, saplings in trees.items():
        i, j = location
        saplings.sort()
        tmp = []
        # 죽은 나무의 양분을 저장하는 변수 nutrition
        nutrition = 0
        for sapling in saplings:
            if land[i][j] >= sapling:
                tmp.append(sapling+1)
                land[i][j] -= sapling
            else:
                nutrition += sapling//2
        # 봄
        if tmp:
            next[(i, j)] = tmp
        # 여름
        land[i][j] += nutrition
    T = defaultdict(list)
    for location, saplings in next.items():
        ci, cj = location
        T[(ci, cj)] = T[(ci, cj)] + saplings
        # 가을
        for tree in saplings:
            if tree%5 == 0:
                for di, dj in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
                    ni, nj = ci+di, cj+dj
                    if 0 <= ni < N and 0 <= nj < N:
                        T[(ni, nj)].append(1)
    trees = T
    # 겨울
    for ii in range(N):
        for jj in range(N):
            land[ii][jj] += A[ii][jj]
# K년이 지난 후 살아남은 나무의 수 answer
answer = 0
for plant in trees.values():
    answer += len(plant)

# answer을 출력
print(answer)