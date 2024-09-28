from collections import defaultdict
import sys

def func():
    return

# 땅의 크기 N, 나무의 그루수 M, 지나는 해 K년
N, M, K = map(int, sys.stdin.readline().split())
# 겨울에 추가 되는 양분의 정보를 저장하는 배열 A
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 땅의 양분을 저장하는 배열 land
land = [[5]*N for _ in range(N)]
# 묘목의 정보를 저장하는 딕셔너리 tree
tree = defaultdict(list)

for _ in range(M):
    # 나무의 위치 x, y, 나무의 나이 z
    x, y, z = map(int, sys.stdin.readline().split())
    tree[(x, y)].append(z)

print(tree)