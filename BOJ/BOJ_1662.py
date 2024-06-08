import sys

# 압출되지 않은 문자열 S
S = list(sys.stdin.readline().rstrip())

# 길이와 K를 저장하는 배열 stack
stack = []
# 길이을 저장하는 변수 cnt, 반복 횟수 K
cnt, K = 0, 0

for s in S:
    if s == '(':
        # K를 제외한 길이 cnt-1와 마지막 수 K를 stack에 저장, cnt값 초기화
        stack.append((cnt-1, K))
        cnt = 0
    elif s == ')':
        # stack에 저장된 마지막 값을 cnt에 압축을 풀어 저장
        # number는 반복횟수 K 앞의 문자열의 길이
        number, K = stack.pop()
        cnt = number+K*cnt
    else:
        # 문자열의 길이 cnt 1 증가, K일 수 있는 값 s를 저장
        cnt += 1
        K = int(s)

# 압축되지 않은 문자열의 길이를 출력
print(cnt)