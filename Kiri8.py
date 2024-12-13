num = int(input("Введите трехзначное число число: "))
if 100 <= num < 999:
    str_num = str(num)
    swapped_num = int(str_num[2] + str_num[0] + str_num[1])
else:
    print("Не то)")
print("Хехехе, твое число теперь не твое >:) --->", swapped_num)
