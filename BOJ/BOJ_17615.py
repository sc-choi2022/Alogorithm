import sys

# 볼의 총 개수 N
N = int(sys.stdin.readline())
# 볼의 색상을 저장하는 배열 colours
colours = sys.stdin.readline().rstrip()

# 좌측으로 레드 모으는 횟수
redL = colours.lstrip('R').count('R')
# 우측으로 레드 모으는 횟수
redR = colours.rstrip('R').count('R')

# 좌측으로 블루 모으는 횟수
blueL = colours.lstrip('B').count('B')
# 우측으로 블루 모으는 횟수
blueR = colours.rstrip('B').count('B')

answer = min(redL, redR, blueL, blueR)
# 최소 이동횟수를 출력
print(answer)