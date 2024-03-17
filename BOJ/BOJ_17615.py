import sys

# 볼의 총 개수 N
N = int(sys.stdin.readline())
# 볼의 색상을 저장하는 배열 colours
colours = sys.stdin.readline().rstrip()
# 최소 이동횟수 answer
answer = len(colours)

# 우측으로 레드 모으는 횟수
redR = colours.rstrip('R')
answer = min(answer, redR.count('R'))
# 우측으로 블루 모으는 횟수
blueR = colours.rstrip('B')
answer = min(answer, blueR.count('B'))
# 좌측으로 레드 모으는 횟수
redL = colours.lstrip('R')
answer = min(answer, redL.count('R'))
# 좌측으로 블루 모으는 횟수
blueL = colours.lstrip('B')
answer = min(answer, blueL.count('B'))

print(answer)