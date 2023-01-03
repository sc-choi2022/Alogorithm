import sys

# 탑의 수 N
N = int(sys.stdin.readline())
# 탑들의 높이를 담을 배열 towers
towers = list(map(int, sys.stdin.readline().split()))
stack = towers.copy()
stack.pop()

ans = [0] * N

for i in range(N - 1, 0, -1):
    while stack:
        temp = stack.pop()

        if temp >= towers[i]:
            ans[i] = len(stack) + 1
            print(stack)
            break
print(*ans)