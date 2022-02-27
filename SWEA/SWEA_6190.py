import sys
sys.stdin = open('s_input.txt')

# 테스트 케이스의 수 T
T = int(input())
for case in range(1, T+1):
    # 양의 정수 A의 개수
    N = int(input())
    # A들의 값을 담은 리스트 A
    A = list(map(int, input().split()))
    # Ai x Aj값이 단조 증가하는 수의 리스트를 리스트 ans
    ans = 0

    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            # 단조증가를 확인하기 위해 각 단위의 값을 담을 tmp, 정렬된 tmp를 담을 s_tmp이 될 리스트 초기화
            tmp = []
            s_tmp = []

            # 단조 증가하는 Ai x Aj temp
            temp = A[i]*A[j]
            ans.append(temp)
            # temp의 각 단위의 값을 리스트 tmp에 담는다.
            while temp>0:
                tmp = [temp%10] + tmp
                temp = temp//10
            s_tmp = sorted(tmp)
            # temp가 단조증가라면 리스트 ans에 추가
            if tmp != s_tmp:
                ans.pop()
    ans.sort()
    if ans == []:
        result = -1
    else:
        result = ans[-1]
    # 테스트케이스 번호 출력
    print(f'#{case} {result}')