# 주어지는 숫자 N
N = int(input())

# 중앙에서 멀어지는 원의 가장 작은 값을 가이드라인 값
# 첫 값은 중앙의 1
checknumber = 1
# 원의 위치 cnt
cnt = 1

while N > checknumber:
    # 현재 원위치의 가장 작은 값은 6의 배수로 커진다.
    checknumber += 6*cnt
    # 다음 원의 위치로 + 1
    cnt += 1

# 현재 원의 위치만큼 움직이는 것이므로 cnt를 출력
print(cnt)