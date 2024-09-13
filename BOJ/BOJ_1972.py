import sys

def func(s):
    for idx in range(1, len(s)):
        check = set()
        for i in range(len(s)-idx):
            pair = s[i] + s[i+idx]
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