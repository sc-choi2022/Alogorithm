from itertools import permutations
import sys

def method(previous, number, S, B):
    lst = []
    number = str(number)
    for able in previous:
        tmp = ''.join(able)
        # 스트라이크 조건이 성립하는 경우
        if int(tmp[0] == number[0]) + int(tmp[1] == number[1]) + int(tmp[2] == number[2]) == S:
            cnt = 0
            for a in able:
                if a in number:
                    cnt += 1
            if cnt - S == B:
                lst.append(able)
    return lst

# 질문횟수 N
N = int(sys.stdin.readline())

# 첫번째 숫자 number와 스트라이크 개수 S, 볼의 개수 B
number, S, B = map(int, sys.stdin.readline().split())
candidates = method(permutations([str(i) for i in range(1, 10)], 3), number, S, B)

for _ in range(N-1):
    # 질문한 숫자 number, 스트라이크 개수 S, 볼의 개수 B
    number, S, B = map(int, sys.stdin.readline().split())
    candidates = method(candidates, number, S, B)
# 가능성이 있는 답의 총 개수를 출력
print(len(candidates))