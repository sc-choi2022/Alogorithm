import sys

# 이동하려고 하는 채널 N
N = int(sys.stdin.readline())
# 고장난 버튼의 개수 M
M = int(sys.stdin.readline())
# 고장난 버튼을 담은 리스트 wrong
wrong = set(sys.stdin.readline().rstrip().split()) if M else set()
answer = abs(100-N)
for num in range(1000001):
    for n in str(num):
        if n in wrong:
            break
    else:
        answer = min(answer, len(str(num)) + abs(num - N))
print(answer)