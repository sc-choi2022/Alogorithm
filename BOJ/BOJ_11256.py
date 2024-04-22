import sys

# 테스트 케이스 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 사탕의 개수 J, 상자의 개수 N
    J, N = map(int, sys.stdin.readline().split())
    # 상자의 길이를 저장하는 배열 boxes
    boxes = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    boxes.sort(key=lambda x:(-x[0]*x[1]))

    # 최소한의 상자 개수 answer
    answer = 0
    # 담을 수 있는 총 크기 total
    total = 0
    for i in range(N):
        total += boxes[i][0] * boxes[i][1]
        # 사탕을 모두 담을 수 있는 경우 i+1 출력
        if total >= J:
            print(i+1)
            break