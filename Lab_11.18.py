# Andrew Li
# 1824794

input_list = input().split(" ")
for i in range(0, len(input_list)):
    input_list[i] = int(input_list[i])
input_list.sort()
# print(input_list)  # for debugging

for num in input_list:
    if num >= 0:
        print(num, end=' ')
