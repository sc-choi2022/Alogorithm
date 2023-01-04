from collections import deque
import sys

# 물이 새는 곳의 개수 N과 테이프의 길이 L
N, L = map(int, sys.stdin.readline().split())
# 물이 새는 곳의 위치
leak = deque(sorted(list(map(int, sys.stdin.readline().split()))))

# 테이프의 시작 위치 location
location = leak[0] - 0.5
# 테이프의 개수 cnt
cnt = 1

# 물세는 곳을 다 확인할 때 까지
while leak:
    # 물세는 곳 l
    l = leak.popleft()

    # 테이프가 붙은 위치에서 l의 위치까지 수리가능 한 경우 continue
    if l - 0.5 >= location and l + 0.5 <= location + L:
        continue
    # 테이프를 다시 붙여야하는 경우
    else:
        # 테이프의 시작 위치를 재설정, cnt 1 증가
        location = l - 0.5
        cnt += 1
# cnt 출력
print(cnt)