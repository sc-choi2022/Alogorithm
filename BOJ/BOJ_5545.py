import sys

# 토핑의 종류의 수 N
N = int(sys.stdin.readline())
# 도우의 가격 A, 토핑의 가격 B
A, B = map(int, sys.stdin.readline().split())
# 도우의 열량 C
C = int(sys.stdin.readline())
# 토핑의 열량을 저장하는 배열 topping
topping = sorted(list(int(sys.stdin.readline()) for _ in range(N)), reverse=True)

# 최고의 피자의 1원 당 열량 answer
answer = C / A

tmp_T, tmp_C = C, A
for i in range(N):
    tmp_T += topping[i]
    tmp_C += B
    if tmp_T / tmp_C > answer:
        answer = tmp_T / tmp_C
    else:
        break

# 최고의 피자의 1원 당 열량을 출력
print(int(answer))