import sys

# 랜선의 개수 K, 그리고 필요한 랜선의 개수 N
K, N = map(int, sys.stdin.readline().split())
# 가지고 있는 각 랜선의 길이을 담을 배열 length
length = [int(sys.stdin.readline()) for _ in range(K)]
# 이분탐색을 위해 start, end 변수에 1과 max(length) 값을 저장
start, end = 1, max(length)

while start <= end:
    mid = (start + end)//2

    # 만들 수 있는 랜선의 개수를 저장할 변수 cnt
    cnt = 0
    for l in length:
        cnt += (l // mid)
    # cnt가 N보다 작은 경우 mid값이 크므로 end값을 조정
    if cnt < N:
        end = mid - 1
    # cnt가 N개 이상이 가능하므로 최대길이를 위해 start값을 조정
    else:
        start = mid + 1
# end값을 출력
print(end)