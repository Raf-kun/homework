num = int(input("Введите трехзначное число число: "))
if 100 <= num < 999:
    str_num = str(num)
    swapped_num = int(str_num[0] + str_num[1] + str_num[2])
    swapped_num2 = int(str_num[0] + str_num[2] + str_num[1])
    swapped_num3 = int(str_num[1] + str_num[0] + str_num[2])
    swapped_num4 = int(str_num[2] + str_num[1] + str_num[0])
    swapped_num5 = int(str_num[2] + str_num[0] + str_num[1])
    swapped_num6 = int(str_num[1] + str_num[2] + str_num[1])
else:
    print("Не то)")
print("Хехехе, твое число теперь не твое >:) --->", swapped_num)
print("Хехехе, твое число теперь не твое >:) --->", swapped_num2)
print("Хехехе, твое число теперь не твое >:) --->", swapped_num3)
print("Хехехе, твое число теперь не твое >:) --->", swapped_num4)
print("Хехехе, твое число теперь не твое >:) --->", swapped_num5)
print("Хехехе, твое число теперь не твое >:) --->", swapped_num6)