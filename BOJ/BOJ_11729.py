def hanoi(N, start, end):
    if N == 1:
        print(start, end)
        return

    hanoi(N-1, start, 6 - start - end)  # 첫번째 장대의 N-1개의 원판을 중간 장대으로 옮긴다.
    print(start, end)   # 첫번째 장대에서 남은 1개의 원판을 1번 장대에서 마지막 장대로 옮긴다.
    hanoi(N-1, 6 - start - end, end)    # 중간 장대의 N-1개의 원판을 마지막 장대로 옮긴다.

# 첫 번째 장대에 쌓인 원판의 개수 N
N = int(input())

# 옮긴 횟수 K를 출력
print(2**N - 1)
# 옮겨야하는 원판의 개수 N, 원판의 위치 1, 이동하기원하는 위치 3
hanoi(N, 1, 3)