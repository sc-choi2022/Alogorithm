import sys
sys.stdin = open('sample_input.txt')

# Test case 개수
test_case = int(input())
for case in range(1, test_case + 1):
    # Test case의 상자 수 N, 변경 횟수 Q
    N, Q = map(int, input().split())
    # 0 으로 초기화된 N개의 상자
    box = [0] * N
    # 1부터 횟수만큼
    for i in range(1, Q + 1):
        # 시작 상자 L, 종료 상자 R
        L, R = map(int, input().split())
        # 시작 상자부터 종료 상자까지 위치와 횟수에 맞춰 숫자 변경
        for idx in range(L-1, R):
            box[idx] = i
    # 테스트 케이스 개수와 N개의 상자에 적혀있는 값 출력
    print(f'#{case}', *box)