import sys

# 삼각수를 저장하는 배열 tri
tri = [i*(i+1) // 2 for i in range(1, 45)]
# 삼각수의 합으로 표현 가능 여부를 저장하는 배열 eureka
eureka = [0] * 1001

for i in tri:
    for j in tri:
        for k in tri:
            if i + j + k <= 1000:
                eureka[i+j+k] = 1

# 테스트 케이스의 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    K = int(sys.stdin.readline())
    # K가 정확히 3개의 삼각수의 합으로 표현될수 있다면 1을, 그렇지 않다면 0을 출력
    print(eureka[K])