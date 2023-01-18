import sys

# A에 담기는 정수의 수 N
N = int(sys.stdin.readline())
# A를 set으로 설정하여 N개의 정수를 저장한다.
A = set(map(int, sys.stdin.readline().split()))
# 주어지는 M개의 정수
M = int(sys.stdin.readline())
# 순서가 중요하므로 list로 M개의 정수를 저장
lstM = list(map(int, sys.stdin.readline().split()))
# M을 순서에 맞에 확인하여 A에 있다면 1, 없다면 0 출력
for M in lstM:
    print(1 if M in A else 0)

# 이분 탐색
import sys
# 이분 탐색을 실행하는 함수 binary
def binary(arr, value):
    first, end = 0, N - 1

    while first <= end:
        mid = (first + end) // 2
        if arr[mid] == value:
            return mid

        if arr[mid] > value:
            end = mid -1
        else:
            first = mid + 1
    return -1

# 정수의 수 N, 정수 N을 담은 배열 lst
N = int(sys.stdin.readline())
lst = sorted(list(map(int, sys.stdin.readline().split())))

# 주어지는 M개의 정수, M개의 정수를 담은 배열 checklist
M = int(sys.stdin.readline())
checklist = list(map(int, sys.stdin.readline().split()))

# checklist의 각 정수를 binary함수를 통해 확인 후 0 혹은 1을 출력
for c in checklist:
    number = binary(lst, c)
    print(0) if number == -1 else print(1)