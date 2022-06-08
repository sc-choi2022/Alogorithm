import sys
# 수열 A의 크기 N
N = int(input())

# A의 원소 N개를 리스트 A에 담는다.
A = list(map(int, sys.stdin.readline().split()))
# 출력할 ans를 -1으로 초기화
ans = [-1] * N
# 시간 초과를 해결하기 위해 stack을 활용한다.
stack = []

# A의 N개의 원소에 대해
for i in range(N):
    # stack이 있는 상태에서 stack의 top값이 A[i]보다 작다면
    while stack and (A[stack[-1]] < A[i]):
        # ans의 stack[-1] 즉 stack.pop()의 값을 A[i]로 설정한다.
        ans[stack.pop()] = A[i]

    # while문을 나와서 stack에 i를 추가한다.
    stack.append(i)
# ans를 조건에 맞게 출력한다.
print(*ans)