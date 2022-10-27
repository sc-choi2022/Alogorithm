import sys

while True:
    # 영어 대소문자, ',', '.', '!', '?', 공백으로 이루어진 문장 line
    line = sys.stdin.readline().strip()
    # 입력의 끝인 경우 break
    if line == '#':
        break
    # 출력할 모음의 개수 cnt
    cnt = 0
    # line의 각 알파벳 l 중 모음이 있는 경우 cnt 1 증가
    for l in line:
        if l in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            cnt += 1
    # cnt 출력
    print(cnt)