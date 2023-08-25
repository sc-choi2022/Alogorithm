import sys

# 창문의 개수와 사람의 개수 N
N = int(sys.stdin.readline())
# 열려있는 창문의 개수 answer
answer = 0
x = 1

while x**2 <= N:
    x += 1
    answer += 1
# 열려있는 창문의 개수 answer 출력
print(answer)