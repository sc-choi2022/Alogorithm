import sys, string

# 문자열 S
S = sys.stdin.readline().rstrip()

# 딕셔너리에 문자열 S의 모든 소문자 정보를 리스트로 담는다.
char_cnt = {}
# string.ascii_lowercase의 모든 소문자에 대해 문자열의 누적개수를 담는다.
for char in string.ascii_lowercase:
    char_cnt[char] = [0]*(len(S)+1)
    cnt = 0
    for idx, value in enumerate(S):
        if value == char:
            cnt += 1
        char_cnt[char][idx+1] = cnt

# 질문의 수 q
q = int(sys.stdin.readline())
# 질문을 확인하여 나타나는 횟수 출력
for _ in range(q):
    alpha, l, r = sys.stdin.readline().split()
    print(char_cnt[alpha][int(r)+1] - char_cnt[alpha][int(l)])