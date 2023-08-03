import sys

# 스크린 칸의 개수 N, 스크린의 아래쪽 칸의 개수 M
N, M = map(int, sys.stdin.readline().split())
# 칸의 범위 A, B
A, B = 0, M-1
# 떨어지는 사과의 개수 J
J = int(sys.stdin.readline())
# 바구니의 이동 거리의 최솟값 answer
answer = 0

for _ in range(J):
    # 사과가 떨어지는 칸 D
    D = int(sys.stdin.readline()) - 1
    while True:
        if A <= D <= B:
            break
        elif D > B:
            A += 1
            B += 1
            answer += 1
        else:
            A -= 1
            B -= 1
            answer += 1
# 모든 사과를 담기 위해서 바구니가 이동해야 하는 거리의 최솟값을 출력
print(answer)