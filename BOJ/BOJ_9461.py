import sys

# 나선에 있는 N번째 정삼각형의 변을 구하는 함수 findK
def findK(N):
    # N < 11이면 return
    if N < 11 or triangle[N]:
        return
    # N이 11이상이면 for문으로 K을 구해준다.
    for i in range(11, N + 1):
        # i번째 삼감형이 구해졌다면 continue
        if triangle[i]:
            continue
        # K의 규칙에 따라 구한다.
        triangle[i] = triangle[i-1] + triangle[i-5]

# 테스트 케이스 T
T = int(sys.stdin.readline())
# N번째 길이 K을 triangle[N]에 담는 리스트 triangle
triangle = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 90

for _ in range(T):
    # 정수 N
    N = int(sys.stdin.readline())
    # findK(N) 실행
    findK(N)
    # triangle[N] 출력
    print(triangle[N])