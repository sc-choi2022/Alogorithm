import sys

# 테스트 케이스 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 오셀로 말의 개수 N
    N = int(sys.stdin.readline())
    # 오셀로 말의 초기 상태
    origin = sys.stdin.readline().rstrip()
    # 오셀로 말의 목표 상태
    goal = sys.stdin.readline().rstrip()
    # 둘의 다른 개수 tmp, origin, goal의 검은돌 개수 b1, b2
    tmp, b1, b2 = 0, origin.count('B'), goal.count('B')
    for i in range(N):
        if origin[i] != goal[i]:
            tmp += 1
    # 검은 말의 개수 차이 cnt
    cnt = abs(b1-b2)
    # 초기 상태에서 목표 상태를 만들기 위한 작업의 최소 횟수 출력
    print(cnt + (tmp-cnt)//2)