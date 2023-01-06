import sys

# 탑의 수 N
N = int(sys.stdin.readline())
# 탑들의 높이를 담을 배열 towers
towers = list(map(int, sys.stdin.readline().split()))
# 스택으로 사용할 배열 stack
stack = []

for i in range(N):
    # i + 1번째 탑의 높이 h
    h = towers[i]

    if stack:
        while stack:
            # 레이저를 만날 수 없는 탑을 확인한 경우
            if stack[-1][0] < h:
                # stack.pop()
                stack.pop()
                # stack.pop() 후 stack이 비었다면 0을 출력
                if not stack:
                    print(0, end=' ')
            # 레이저를 만나는 탑을 확인한 경우
            else:
                # 탑의 번호를 출력 후 break
                print(stack[-1][1], end=' ')
                break

        # while문을 나온 후 stack에 현재 탑의 높이와 번호를 저장
        stack.append((h, i + 1))
    # stack이 비어있다면
    else:
        # 0을 출력 후 stack에 현재 높이와 탑의 번호를 tuple로 저장
        print(0, end=' ')
        stack.append((h, i + 1))