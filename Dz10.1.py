num1 = int(input("Введите число:"))
num2 = int(input("Введите второе число:"))
list_of_numbers = []

for i in range(num1, num2 + 1):
    if i == 1:
        list_of_numbers append(i)
    else:
        for i in range(2, i):
            if i % j == 0:
                list_of_numbers append(i)

print(set(list_of_numbers append))
