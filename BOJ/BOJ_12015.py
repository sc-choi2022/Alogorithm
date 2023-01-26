import sys

# 수열 A의 크기 N
N = int(sys.stdin.readline())

# 수열 A
A = list(map(int, sys.stdin.readline().split()))
# LIS를 담을 배열 LIS, 초기에 값 0을 저장한다.
LIS = [0]

for a in A:
    # LIS의 첫 값을 정하는 부분
    if LIS[-1] < a:
        LIS.append(a)
    # a의 위치를
    else:
        start, end = 0, len(LIS)

        while start < end:
            mid = (start + end) // 2

            if LIS[mid] < a:
                start = mid + 1
            else:
                end = mid
        LIS[end] = a
# LIS의 초기에 저장한 값 0을 제거
LIS.pop(0)
# 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력
print(len(LIS))