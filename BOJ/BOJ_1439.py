numb = list(map(int,input())) # 문자열 S의 각 숫자를 담은 리스트 numb

cnt = [0, 0]    # index값의 위치에 index 숫자를 한번에 뒤집을 수 있는 묶음의 수를 담는다.
now = numb[0]   # 첫 숫자를 now에 할당
cnt[now] = 1    # now 숫자의 묶음 1 증가
for i in range(1, len(numb)):   # 나머지 숫자에 대해
    if now != numb[i]:          # 현재 숫자와 다르면
        cnt[numb[i]] += 1       # 숫자 index의 묶음 수 1증가 후
        now = numb[i]           # now 값 numb[i]로 재설정
print(min(cnt))                 # 리스트 cnt 중 min 값 출력