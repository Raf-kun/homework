num = int(input("Введите трехзначное число: "))
desyatki = num // 10
edinitsi = num % 10
summa = desyatki + edinitsi
print(f"В числе {num},\n десятки - {desyatki},\n"
                f"единицы - {edinitsi},\n сумма - {summa}")
