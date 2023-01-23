# 상근이가 가진 카드의 개수 N
N = int(input())
# 상근이의 카드에 적힌 숫자 N개를 담은 S
S = list(map(int, input().split()))

# 시간 초과를 해결하기 위해 딕셔너리를 사용하여 상근이의 카드 정보를 저장한다.
dic = dict()
for s in S:
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

# 주어지는 숫자의 개수 M
M = int(input())
# M개의 숫자를 담은 리스트 G
G = list(map(int, input().split()))

# G의 모든 값들 중
for g in G:
    # dic에 있다면 g에 맞는 value값을 출력
    if g in dic:
        print(dic[g], end=' ')
    # dic에 없다면 0을 출력
    else:
        print(0, end=' ')

# 이분탐색
import sys

def binary(c, bound):
    start, end = 0, N

    while start < end:
        mid = (start + end) // 2
        # lowerbound인 경우
        if bound == 0:
            if numbers[mid] < c:
                start = mid + 1
            else:
                end = mid
        # upperbound인 경우
        else:
            if numbers[mid] <= c:
                start = mid + 1
            else:
                end = mid
    # bound의 기준이되는 위치를 return
    return end

# 숫자카드의 개수 N
N = int(sys.stdin.readline())
# N개의 숫자카드를 저장하는 배열 numbers, 정렬
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
# 주어지는 정수의 개수 M
M = int(sys.stdin.readline())
# M개의 정수를 담을 배열 check
check = list(map(int, sys.stdin.readline().split()))
# check의 모든 정수의 개수를 함수 binary를 활용하여 구한다.

for c in check:
    # upperbound의 return값과 lowerbound의 return값의 차를 출력
    print(binary(c, 1) - binary(c, 0), end=' ')