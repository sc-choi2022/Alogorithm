import sys

# 테스트 케이스의 수 P
P = int(sys.stdin.readline())

for _ in range(P):
    # 테스트 케이스 번호 T, 줄 서 있는 학생들의 키를 저장하는 배열 heights
    T, *heights = list(map(int, sys.stdin.readline().split()))
    order = [heights[0]]

    answer = 0
    for i in range(20):
        for j in range(i+1, 20):
            if heights[i] > heights[j]:
                answer += 1
                heights[i], heights[j] = heights[j], heights[i]
                
    # 테스트 케이스의 번호와 학생들이 뒤로 물러난 걸음 수의 총합 출력
    print(T, answer)