def solution(num, total):
    answer = []

    # 중앙값의 정수부분을 변수 mid에 저장
    mid = int(total / num)
    # answer에 mid를 저장
    answer = [mid]
    # 중앙값을 기준으로 가감할 값 idx
    idx = 1
    for i in range(1, num):
        # 홀수번의 경우
        if i%2:
            # mid + idx을 answer에 저장
            answer.append(mid + idx)
        # 짝수번의 경우
        else:
            # mid - idx을 answer에 저장, idx 1 증가
            answer.append(mid - idx)
            idx += 1
    # answer을 정렬
    answer.sort()
    return answer