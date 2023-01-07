import sys

# 초기 문자열 stringA
stringA = list(sys.stdin.readline().rstrip())
# 커서로 인해 옮겨지는 값을 담을 배열 stringB
stringB = []

# 명령어의 개수 M
M = int(sys.stdin.readline())

for i in range(M):
    # 명령어
    command = sys.stdin.readline().rstrip().split()
    # 명령어가 P인 경우
    if len(command) == 2:
        stringA.append(command[1])
    else:
        command = command[0]
        # 명령어가 L이고 커서가 맨앞이 아닌 경우
        if command == 'L' and stringA:
            stringB.append(stringA.pop())
        # 명령어가 D이고 커서가 맨뒤가 아닌 경우
        elif command == 'D' and stringB:
            stringA.append(stringB.pop())
        # 명령어가 B이고 커서가 맨앞이 아닌 경우
        elif command == 'B' and stringA:
            stringA.pop()
# 모든 명령어를 수행 후 편집기에 입력되어 있는 문자열
print(''.join(stringA + list(reversed(stringB))))