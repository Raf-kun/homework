num = int(input("Введите число в диопозоне от 1 до 100: "))
if num < 1 or num > 100:
    print("Число не в диапfзоне!")
elif num % 3 == 0 and num % 5 == 0:
    print("Fizz Buzz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0:
    print("Fizz")
else:
    print(num)