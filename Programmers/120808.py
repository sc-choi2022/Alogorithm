from math import gcd

def solution(numer1, denom1, numer2, denom2):
    # 더한 값의 분자 numer3, 분모 denom3
    numer3 = numer1 * denom2 + numer2 * denom1
    denom3 = denom1 * denom2
    # numer3와 denom3의 공약수
    GreatestCommonDivisor = gcd(numer3, denom3)
    # 기약분수의 분자 분모를 순서대로 담은 배열 answer
    answer = [numer3//GreatestCommonDivisor, denom3//GreatestCommonDivisor]

    return answer