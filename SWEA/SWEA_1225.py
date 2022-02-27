import sys, collections
sys.stdin = open('input.txt')

for _ in range(10):
    case = int(input())
    # 8개의 숫자를 입력받고 deque를 활용하여 q에 할당
    q = collections.deque(list(map(int, input().split())), maxlen = 8)

    # 사이클에서 감소시키는 값 i를 첫번째 사이클 값이 1로 초기화
    i = 1
    # 1부터 5까지 감소시키는 사이클을 while문으로 통해 실행
    while True:
        # i가 사이클의 마지막 값 5을 넘었다면 다시 1로 초기화
        if i > 5:
            i = 1
        # q의 첫번째 값을 pop을 꺼내서 사이클에 맞게 i를 감소
        in_q = q.popleft() - i
        # 숫자가 감소할 때 0보다 작아지는 경우
        if in_q <= 0:
            # 0으로 유지한채 종료
            q.append(0)
            break
        # 숫자가 0보다 큰 경우 q의 마지막 값에 추가
        q.append(in_q)
        # 사이클에 따라 1 추가
        i += 1

    # 테스트케이스의 번호와 답을 출력
    print(f'#{case}', *list(q))