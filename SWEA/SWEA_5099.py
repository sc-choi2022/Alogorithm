from collections import deque
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T+1):
    # 화덕에 들어갈 수 있는 피자수 N, 총 피자 수 M
    N, M = map(int, input().split())
    # 치즈의 양을 담은 리스트 cheeze
    cheeze = list(enumerate(list(map(int, input().split())), 1))
    # queue형태의 oven과 완성된 순서대로 피자의 순서를 담을 리스트 pizza
    oven = deque()
    pizza = []

    # oven을 가득 차도록 채운다.
    for _ in range(N):
        oven.append(cheeze.pop(0))

    # oven이 비어있게 될 때까지 진행
    while oven:
        # oven이 가득 차 있지 않고 cheeze이 비어있지 않다면 oven에 cheeze[0]을 추가
        if len(oven) < N and cheeze:
            oven.append(cheeze.pop(0))

        idx, ch = oven.popleft()
        # 치즈가 여전히 남아 있다면
        if ch//2 != 0:
            # 치즈를 절반으로 줄이고 oven에 추가
            oven.append([idx, ch//2])
        else:
            # 치즈가 녹아 피자 완성 시 리스트 pizza에 피자의 번호 추가
            pizza.append(idx)
    # 테스트케이스 번호와 pizza[-1] 값을 출력
    print(f'#{case} {pizza[-1]}')