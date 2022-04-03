import sys
sys.stdin = open('sample_input.txt')

# 확인할 리스트와 idx의 위치를 활용하는 함수
def check(arr, idx):
    # triplet 여부 확인
    if arr[idx] == 3:
        return True
    # run 여부 확인
    for i in range(len(arr) - 3 + 1):
        if arr[i: i+3].count(0) == 0:
            return True
    return False

T = int(input())
for case in range(1, T+1):
    # 카드의 정보를 담은 리스트 arr
    arr = list(map(int, input().split()))
    # p1, p2는 각각 플레이어가 소지한 숫자를 index로 개수를 세는 리스트
    p1 = [0]*10
    p2 = [0]*10
    # 결과 ans값을 0으로 초기화
    ans = 0
    # 총 12개의 카드에 대해
    for i in range(12):
        # 순서에 따라 분배하고 p1, p2에 받은 카드 수를 반영
        if i % 2 == 0:
            p1[arr[i]] += 1
            # check 함수가 true라면 ans 1로 저장 후 break
            if check(p1, arr[i]):
                ans = 1
                break
        else:
            p2[arr[i]] += 1
            # check 함수가 true라면 ans 1로 저장 후 break
            if check(p2, arr[i]):
                ans = 2
                break
    # 테스트 케이스번호와 ans 출력
    print(f'#{case} {ans}')