# 집의 개수 N, 공유기 개수 C
N, C = map(int, input().split())
lst = [0] * N
for i in range(N):
    lst[i] = int(input())
# 집의 위치를 정렬
lst.sort()
# 최소거리 start
start = 1
# 최대 거리 end
end = lst[-1] - lst[0]
# 출력할 정답 ans 초기화
ans = 0

while start <= end:
    mid = (start + end ) // 2 # 최소 거리와 최대 거리의 중간값
    first = lst[0]
    cnt = 1

    # 중간 값을 기준으로 집의 개수를 센다.
    for j in range(1, N):
        if lst[j] >= first + mid:
            cnt += 1
            first = lst[j]

    # 집의 개수가 c보다 크다면 초소값을 중간값 +1로 갱신한다.
    if cnt >= C:
        start = mid + 1
        ans = mid
    # 집의 개수가 c보다 작다면 중간값 -1로 갱신한다.
    else:
        end = mid - 1
# 최대 간격을 출력한다.
print(ans)