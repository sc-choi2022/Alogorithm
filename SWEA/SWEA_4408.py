import sys
sys.stdin = open('sample_input.txt')

# 테스트 케이스 T
T = int(input())
for case in range(1, T+1):
    # 돌아가야 할 학생들의 수 N
    N = int(input())
    # 방 번호 <= 400
    corridor = [0]*200

    # 학생의 수 만큼
    for i in range(N):
        # 현재 방과 이동할 방 번호를 받아서
        temp = list(map(int, input().split()))
        # 방 번호가 홀수인지 짝수 인지 구분하여 현재에서 복도의 위치로 값을 재설정
        # 리스트가 0부터 인것을 고려하여 재설정
        for j in range(2):
            if temp[j]%2 == 1:
                temp[j] = (temp[j]-1)//2
            else:
                temp[j] = (temp[j]-2)//2

        # 큰 수에서 작은 수로 오는 경우
        # for문이 달라지므로 작은 값이 temp[0]되도록 교체
        if temp[0] > temp[1]:
            temp[0], temp[1] = temp[1], temp[0]

        # 작은 방번호에서 큰 방번호로 갈때 지나는 복도에 1 증가
        for c in range(temp[0], temp[1]+1):
            corridor[c] += 1
    # 테스트 케이스 번호와 필요한 시간 출력
    print(f'#{case} {max(corridor)}')