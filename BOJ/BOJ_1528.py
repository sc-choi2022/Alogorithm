import sys

def gold(number, something):
    global answer

    if number == 0:
        return 

    for i in range(len(str(number)), 0, -1):
        if number >= int('4'*i) and not visit[number-int('4'*i)]:
            something.append('4'*i)
            visit[number-int('4'*i)] = 1
            gold(number-int('4'*i), something)
            visit[number-int('4'*i)] = 0
            something.pop()
        if number >= int('7'*i) and not visit[number-int('7'*i)]:
            something.append('7'*i)
            visit[number-int('7'*i)] = 1
            gold(number-int('7')*i, something)
            visit[number-int('7')*i] = 0
            something.pop()

N = int(sys.stdin.readline())
visit = [0]*(N+1)
answer = []
visit[N] = 1
gold(N, [])
print(answer)
print(['4', '7'] < ['7', '4'])