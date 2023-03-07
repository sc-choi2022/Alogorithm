def solution(common):
    answer = 0
    # 1항, 2항, 3항을 변수 first, second, third에 저장
    first, second, third = common[:3]
    # 마지막항 last
    last = common[-1]
    # 등차수열인 경우
    if second - first == third - second:
        # 마지막 항의 값에 등차를 다한다.
        answer = last + second - first
    # 등비수열인 경우
    elif second // first == third // second:
        # 마지막 항의 값에 등비를 곱한다.
        answer = last * second // first
    return answer