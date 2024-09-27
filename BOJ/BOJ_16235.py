import sys

def func():
    return

# 땅의 크기 N, 나무의 그루수 M, 지나는 해 K년
N, M, K = map(int, sys.stdin.readline().split())
# 나무의 정보를 저장하는 배열 trees
trees = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for _ in range(K):
    func()

print(answer)