import sys

# 숫자를 모니터 형식에 맞게 변형하는 함수 digital
def digital(number):
    lcd = [[' '] * (S + 2) for _ in range(2 * S + 3)]
    if number in '23567890':
        for j in range(1, S+1):
            lcd[0][j] = '-'
    if number in '045689':
        for j in range(1, S+1):
            lcd[j][0] = '|'
    if number in '01234789':
        for j in range(1, S+1):
            lcd[j][S+1] = '|'
    if number in '2345689':
        for j in range(1, S+1):
            lcd[S+1][j] = '-'
    if number in '0268':
        for j in range(S+2, 2*S+2):
            lcd[j][0] = '|'
    if number in '013456789':
        for j in range(S+2, 2*S+2):
            lcd[j][S+1] = '|'
    if number in '0235689':
        for j in range(1, S+1):
            lcd[2*S+2][j] = '-'
    return lcd


# 크기 S, 모니터에 나타내야할 수 N
S, N = sys.stdin.readline().rstrip().split()
S = int(S)

# 모니터에 나타나는 숫자를 저장하는 배열 screen
screen = [digital(N[i]) for i in range(len(N))]

# 출력
for line in zip(*screen):
    for l in line:
        print(''.join(l), end=' ')
    print()