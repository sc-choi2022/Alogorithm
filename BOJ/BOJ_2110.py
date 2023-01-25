import sys

# 집의 개수 N, 공유기의 개수 C
N, C = map(int, sys.stdin.readline().split())

# 집의 좌표를 담을 배열 site
site = [int(sys.stdin.readline()) for _ in range(N)]
site.sort()

# 이분탐색을 위한 start, end
start, end = 0, site[-1] - site[0]

while start <= end:
    mid = (start + end) // 2
    # mid를 더해 가능한 위치를 확인하는 위치
    place = site[0]
    # 설치가능한 공유기수 cnt, 첫번째 place의 위해에 공유기 설치
    cnt = 1

    # 설치가능한 위치를 확인 후 cnt에 반영
    for i in range(1, N):
        if site[i] >= place + mid:
            cnt += 1
            place = site[i]

    # C개 이상의 공유기설치가 가능한 경우 start값을 조정
    if cnt >= C:
        start = mid + 1
    # C개의 공유기설치가 불가능한 경우 end값을 조정
    else:
        end = mid - 1
# 가장 인접한 두 공유기 사이의 최대 거리를 출력
print(end)