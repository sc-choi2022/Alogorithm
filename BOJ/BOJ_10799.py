import sys

# 쇠막대기와 레이저의 배치를 나타내는 괄호 표현을 담을 배열 stack
stack = list(sys.stdin.readline().rstrip())

# 현재 확인하는 막대기의 개수
cnt = 0
# 출력할 조각의 총 개수
ans = 0

while stack:
    # stack.pop()의 반환값을 piece에 저장한다.
    piece = stack.pop()
    # piece가 )이고
    if piece == ')':
        # 레이저인 경우
        if stack[-1] == '(':
            # 현재 막대기의 개수만큼 조각의 개수 ans에 저장 후 레이저의 (을 제거
            ans += cnt
            stack.pop()
        # 막대기의 시작을 의미하는 경우
        else:
            # 막대기의 개수 cnt 1 증가
            cnt += 1
    # 막대기가 끝난 경우
    else:
        # 막대기의 개수 1 감소, 조각의 개수 1 증가
        cnt -= 1
        ans += 1
# 잘려진 조각의 총 개수를 출력
print(ans)