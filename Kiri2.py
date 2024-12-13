num = int(input("Введите двузначное число: "))
if 10 <= num < 100:
    str_num = str(num)
    swapped_num = int(str_num[1] + str_num[0])
else:
    print("Не то)")
print("Хехехе, твое число теперь не твое >:) --->", swapped_num)
