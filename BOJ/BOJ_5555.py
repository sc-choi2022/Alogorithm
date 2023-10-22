import sys

# 찾고자하는 문자열 string
string = sys.stdin.readline().rstrip()
L = len(string)
# 반지의 개수 N
N = int(sys.stdin.readline())
# 문자열을 포함하는 반지의 개수 answer
answer = 0

for _ in range(N):
    ring = sys.stdin.readline().rstrip()
    M = len(ring)
    ring += ring
    for i in range(M+1):
        if string == ring[i:i+L]:
            answer += 1
            break
# 찾고자하는 문자열을 포함 반지의 개수를 나타내는 정수를 한 줄로 출력
print(answer)