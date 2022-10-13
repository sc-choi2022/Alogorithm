import sys

answers = [0, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 2] + [6]*1000000
six = [0]*1000000
def makesix(N):
    i = 1
    for i in range(1000000)
        tmp = (i-1)*6 + six[i-1] - (2*(i-2)+1)
        if tmp > N:
            return six
        six[i] = tmp

N = int(sys.stdin.readline())
if N < 13:
    print(answers[N])
    exit()

six = makesix(N)

for i in range(13, N + 1):
    ans = 6
    for k in six:
        if k > i:
            break
        ans = min(ans, answers[i-k])
    answers[i] = ans + 1
print(answers[N])