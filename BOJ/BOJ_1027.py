import sys

# 빌딩의 총 개수 N
N = int(sys.stdin.readline())
# 빌딩의 높이를 저장하는 배열 heights
heights = [0] + list(map(int, sys.stdin.readline().split()))
# 보이는 빌딩의 수 answer
answer = 0

for i in range(1, N+1):
    # 기준이 되는 i번째의 좌표
    print(i, heights[i])
    # 비교대상 기울기
    slope = 'notdefined'
    print('기준에 따른 좌측의 기울기')
    for j in range(1, i):
        tmp = (i-j)/(heights[i]-heights[j]) if heights[i] != heights[j] else 0

    #
    print('기준에 따른 우측의 기울기')
    for k in range(i+1, N+1):
        print((i-k)//(heights[i]-heights[k]) if heights[i] != heights[k] else 'zerodivision')

    print('====================================')