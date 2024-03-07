import sys

# 빌딩의 개수 N
N = int(sys.stdin.readline())
# 빌딩의 높이를 저장하는 배열 heights
heights = [int(sys.stdin.readline()) for _ in range(N)]
# 벤치마킹이 가능한 빌딩의 수의 합 answer
answer = 0

# 활용할 스택 stack
# 스택에는 현재 빌딩의 높이보다 높은 빌딩의 수가 저장된다.
# 이는 현재 빌딩을 볼 수 있는 좌측의 빌딩의 수와 동일하다.
stack = []

for height in heights:
    while stack and stack[-1] <= height:
        stack.pop()
    answer += len(stack)
    stack.append(height)
# 관리인들이 벤치마킹이 가능한 빌딩의 수의 합을 출력
print(answer)