# 상근이가 가진 숫자 카드의 개수 N
N = int(input())
# 상근이가 가진 카드의 N개의 숫자를 담을 리스트 numberN
numberN = set(map(int,input().split()))
# 존재 여부를 확인할 카드의 개수 M
M = int(input())
# M개의 카드의 숫자들을 담을 리스트 numberM
numberM = list(map(int,input().split()))

# 상근이의 M개의 카드가
for i in range(M):
    # numberN에 포함되어 있다면 1과 공백을 출력하고
    if numberM[i] in numberN:
        print(1, end=' ')
    # 포함되어 있지 않다면 0과 공백을 출력한다.
    else:
        print(0, end=' ')

# 이분탐색
import sys

def binary(c):
    start, end = 0, N - 1

    while start <= end:
        mid = (start + end) // 2
        # c가 numbers에 있다면 1 return
        if numbers[mid] == c:
            return 1
        # c가 numbers[mid]값보다 작은 경우 start값 조정
        elif numbers[mid] < c:
            start = mid + 1
        # c가 numbers[mid]값보다 큰 경우 end값 조정
        else:
            end = mid - 1
    # 값을 찾지 못한 경우 0 return
    return 0

# 상근이가 가진 숫자카드의 개수 N
N = int(sys.stdin.readline())
# 숫자카드를 담을 배열 numbers
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

# 주어지는 정수의 개수 M
M = int(sys.stdin.readline())
# M개의 정수를 담을 배열 check
check = list(map(int, sys.stdin.readline().split()))
# check의 c에 대해 binary함수 실행 후 출력
for c in check:
    print(binary(c), end=' ')