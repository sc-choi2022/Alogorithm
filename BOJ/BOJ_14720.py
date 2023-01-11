import sys

# 우유 가게의 수 N
N = int(sys.stdin.readline())

# 우유 가게 정보 0 딸기 1 초코 2 바나나
milk = list(map(int, sys.stdin.readline().split()))

# 출력할 마실 수 있는 우유의 최대 개수 ans
ans = 0
# 현재 우유의 상태 -1 초기화
status = -1

for i in range(N):
    # 맨 처음은 딸기우유를 마신다.
    if milk[i] == (status + 1) % 3:
        ans += 1
        status += 1

# ans 출력
print(ans)