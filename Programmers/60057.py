def solution(s):
    L = len(s)
    answer = L

    for i in range(1, L//2+1):
        # i 단위로 나눈 문자열의 길이 tmp, 첫번째 단위 prev와 반복 횟수 cnt
        tmp, prev, cnt = 0, s[:i], 1

        for j in range(i, L + i, i):
            if prev == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    tmp += len(prev)
                else:
                    tmp += len(prev) + len(str(cnt))
                # prev와 cnt 재설정
                prev = s[j:j+i]
                cnt = 1

        answer = min(answer, tmp)
    return answer