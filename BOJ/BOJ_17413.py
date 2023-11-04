import sys
# 문자열 S
S = list(sys.stdin.readline().rstrip())
idx = 0
start = 0
while idx < len(S):
    # 태그의 시작인 경우
    if S[idx] == '<':
        while S[idx] != '>':
            idx += 1
        idx += 1
    # 태그가 아닌 문자인 경우
    elif S[idx].isalnum():
        start = idx
        while idx < len(S) and S[idx].isalnum():
            idx += 1
        S[start:idx] = S[start:idx][::-1]
    # 태그 밖 띄어쓰기 인 경우
    else:
        idx += 1
# 문자열 S의 단어를 뒤집어서 출력
print(''.join(S))