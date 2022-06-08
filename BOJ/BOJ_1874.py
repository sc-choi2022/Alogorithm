# 스택에 넣어줄 수의 개수 N
N = int(input())

# push, pop 의 정보를 담은 리스트 ans
ans = []

stack = []
# 시작 값 num 1로 초기화
num = 1

# 주어지는 N개의 값에 대해
for _ in range(N):
    # input을 받고
    tmp = int(input())
    while True:
        # stack이 비어있지 않고 tmp가 stack의 top의 값과 같다면
        if stack and tmp == stack[-1]:
            # stack.pop()과 ans에 pop 표시 '-'을 추가 후 break
            stack.pop()
            ans.append('-')
            break
        # num값이 N보다 커지면 break
        if num > N:
            break
        # stack에 순서에 맞는 숫자가 없다면 stack에 num 값을 추가하고
        # ans에 push 표시 '+'을 추가한다.
        stack.append(num)
        ans.append('+')
        # num 1증가
        num += 1
# stack에 값이 남아 수열이 완성되지 못했을 경우 NO 출력
if stack:
    print('NO')
# 수열이 완성되었다면 push,pop의 연산을 한 개씩 출력
else:
    for a in ans:
        print(a)