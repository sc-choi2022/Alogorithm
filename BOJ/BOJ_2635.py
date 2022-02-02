data = int(input())
max_cnt = 0

for i in range(data, 0, -1):
    test_list = [data, i]
    first_n = data    
    second_n = i
    next_n = first_n - second_n
    while next_n>=0:
        test_list.append(next_n)
        first_n = second_n
        second_n = next_n
        next_n = first_n - second_n
    cnt = len(test_list)
    if max_cnt <= cnt:
        max_cnt = cnt
        ans_list = test_list

print(max_cnt)
result = ' '.join(map(str,ans_list))
print(result)