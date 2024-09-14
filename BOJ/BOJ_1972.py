import sys

def func(s):
    for d in range(1, len(s)):
        # d-쌍을 저장하는 셋 check
        check = set()
        for i in range(len(s)-d):
            pair = s[i] + s[i+d]
            if pair in check:
                print(f'{s} is NOT surprising.')
                return
            else:
                check.add(pair)
    print(f'{s} is surprising.')

while True:
    # 문자열 S
    S = sys.stdin.readline().rstrip()

    if S == '*':
        break
    # 놀라운(surprising) 문자열인지 아닌지 출력
    func(S)