my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index_ = 0
while index_ < len(my_list):
    num = my_list[index_]
    if num > 0:
        print(num)
    elif num < 0:
        break
    index_ += 1
