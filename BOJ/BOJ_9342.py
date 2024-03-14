import re, sys

# 테스트 케이스의 개수 T
T = int(sys.stdin.readline())
# 규칙의 조건 rule
rule = re.compile('^[A-F]?A+F+C+[A-F]?$')

for _ in range(T):
    # 주어진 염색체 C
    C = sys.stdin.readline().rstrip()
    # 규칙을 지키는 문자열이 아닌 경우에는 "Good"을 출력
    if rule.match(C) == None:
        print('Good')
    # 규칙을 지키는 문자열인 경우에는  "Infected!" 출력
    else:
        print('Infected!')