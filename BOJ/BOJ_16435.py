import sys

# 과일의 개수 N, 스네이크버드의 초기 길이 정수 L
N, L = map(int, sys.stdin.readline().split())
# 과일의 높이를 저장하는 배열 heights
heights = sorted(list(map(int, sys.stdin.readline().split())))

for height in heights:
    if height > L:
        break
    L += 1
# 스네이크버드의 최대 길이 출력
print(L)