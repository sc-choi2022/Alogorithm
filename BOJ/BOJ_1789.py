import sys

# 자연수의 합 S
S = int(sys.stdin.readline())
# S이상이 될때까지 더해줄 값 add
add = 0

# add에 더해 S을 만들어 줄 num 1로 초기화
num = 1

while add < S:
    add += num
    # add와 S이 같은 경우 num 출력 후 break
    if add == S:
        print(num)
        break
    # add > S인 경우 num - 1 출력 후 break
    if add > S:
        print(num - 1)
        break
    # num 1 증가
    num += 1