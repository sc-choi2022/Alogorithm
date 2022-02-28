N = int(input())
max_num = 0
max_lst = []

for i in range(N,0,-1):
    temp_lst = [N, i]
    start = temp_lst[0]
    middle = temp_lst[1]
    end = start - middle
    while True:
        temp_lst.append(end)
        start = middle
        middle = end
        end = start - middle
        if end<0:
            break
    if max_num < len(temp_lst):
        max_num = len(temp_lst)
        max_lst = temp_lst
print(max_num)
print(*max_lst)