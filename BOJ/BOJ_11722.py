import sys

# 수열 A의 N
N = int(sys.stdin.readline())
# 수열 A
A = list(map(int, sys.stdin.readline().split()))
# 가장 긴 부분수열을 담을 배열 LIS
LIS = [1001]

for a in A:
    # LIS[-1]보다 a가 작은 경우
    if LIS[-1] > a:
        LIS.append(a)
    # 배열 LIS에 a의 위치를 배치해야하는 경우
    else:
        # 이분탐색을 위해 start, end값을 저장
        start, end = 0, len(LIS)
        while start < end:
            mid = (start + end) // 2

            if LIS[mid] > a:
                start = mid + 1
            else:
                end = mid
        LIS[end] = a
# 초기에 저장한 값 1001을 제거
LIS.pop(0)
# LIS의 길이를 출력
print(len(LIS))