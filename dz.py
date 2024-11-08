num = int(input("Введите число: "))
degree = int(input("Введите степень: "))
if degree > 0 and degree < 8:
    print(num ** degree)
elif degree == 0:
    print(num ** 0)
else:
    print("Переделывайте...")