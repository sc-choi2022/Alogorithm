import sys

# 링의 개수 N
N = int(sys.stdin.readline())

# N개의 링의 반지름을 담은 리스트 lst
lst = list(map(int, sys.stdin.readline().split()))
# 기준이 되는 첫번째 링 key
key = lst[0]

for i in range(1, N):
    # 분자의 기준이 되는 key를 약분하기 위해 변수 up에 할당
    up = key
    # 분모를 약분하기 위해 변수 down에 lst[i]에 할당
    down = lst[i]
    # 기약분수가 자연수가 되는 경우
    if key%lst[i] == 0:
        # 자연수와 분모에 1을 출력
        print(f'{key//lst[i]}/1')
    else:
        # 약수를 구하기 위해 두 값 중 작은 값 value를 변수에 할당
        value = min(key, lst[i])
        # 약수의 첫 값인 now
        now = 2
        while True:
            # value가 마지막 약수이나 value가 약수가 아니었기때문에 value까지만 확인하고 break
            if now == max(key, lst[i]):
                # 기약분수를 출력 후 break
                print(f'{up}/{down}')
                break
            # 약분이 가능한 경우 up과 down을 재 설정
            if up % now == 0 and down % now == 0:
                up //= now
                down //= now
            else:
                # now 1 증가
                now += 1