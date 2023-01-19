import sys

# 랜선의 개수 K, 그리고 필요한 랜선의 개수 N
K, N = map(int, sys.stdin.readline().split())
# 가지고 있는 각 랜선의 길이을 담을 배열 length
length = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(length)

while start <= end:
    mid = (start + end) // 2
    add = 0

    for l in length:
        add += l // mid

    if add >= N:
        start = mid + 1
    else:
        end = mid - 1
# N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력
print(end)