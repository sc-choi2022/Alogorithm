import sys
# 수행해야하는 연산의 수 M
M = int(sys.stdin.readline())
# 1 <= x <= 20 범위안에 x가 있기 때문에 S의 집합을 리스트로 표시한다.
S = [0] * 21

for _ in range(M):
    # 연산 내용을 words에 할당한다.
    words = list(sys.stdin.readline().split())
    if len(words) == 1:
        # all 연산이라면 S에 모든 x을 1로 저장
        if words[0] == 'all':
            S = [1] * 21
        # empty 연산이라면 S에 모든 x을 0로 저장
        elif words[0] == 'empty':
            S = [0] * 21
        continue
    # 연산 내용의 길이가 2개인 경우
    # command, number에 words[0], int(words[1])을 할당
    command = words[0]
    number = int(words[1])
    # add 연산이면 S[number]에 1 할당
    if command == 'add':
        S[number] = 1
    # remove 연산이면 S[number]에 0 할당
    elif command == 'remove':
        S[number] = 0
    # check 연산이면 S[number]의 값을 확인하고 1이라면 1 출력 아니라면 0 출력
    elif command == 'check':
        print(1) if S[number] else print(0)
    # toggle 연산이면 S[number]
    elif command == 'toggle':
        # S[number]가 있다면 0 할당
        if S[number]:
            S[number] = 0
        # 없다면 1 할당
        else:
            S[number] = 1