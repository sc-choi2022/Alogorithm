import sys

# 빌딩의 총 개수 N
N = int(sys.stdin.readline())
# 빌딩의 높이를 저장하는 배열 heights
heights = [0] + list(map(int, sys.stdin.readline().split()))
# 가장 많은 고층 빌딩에서 보이는 빌딩의 수 answer
answer = 0

for i in range(1, N+1):
    # i번째 빌딩의 좌측에서 볼 수 있는 빌딩의 수
    cnt1 = 0
    # 이전 빌딩과 i번째 빌딩의 기울기
    s1 = None
    for j in range(i-1, 0, -1):
        tmp1 = (heights[j]-heights[i])/(j-i)
        # 첫번째 기울기이거나 이전 기울기 보다 현재 기울기가 작은 경우
        if s1 is None or s1 > tmp1:
            s1 = tmp1
            cnt1 += 1
    # i번째 빌딩의 우측에서 볼 수 있는 빌딩의 수
    cnt2 = 0
    # 이번 빌딩과 i번째 빌딩의 기울기
    s2 = None
    for k in range(i+1, N+1):
        tmp2 = (heights[k]-heights[i])/(k-i)
        # 첫번째 기울기이거나 이전 기울기보다 현재 기울기가 큰 경우
        if s2 is None or s2 < tmp2:
            s2 = tmp2
            cnt2 += 1
    # answer의 값을 갱신
    answer = max(answer, cnt1+cnt2)
# 가장 많은 고층 빌딩이 보이는 빌딩에서 보이는 빌디의 수를 출력
print(answer)