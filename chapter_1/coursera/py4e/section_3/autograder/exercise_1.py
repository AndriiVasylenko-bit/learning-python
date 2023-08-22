# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.
# 3.1 Написать программу, чтобы подсказать пользователю часы и тариф в час, используя ввод для расчета валовой оплаты. Оплата почасовой ставки за часы до 40 часов и 1,5 почасовой ставки за все часы работы свыше 40 часов. Используйте 45 часов и тариф 10,50 в час для тестирования программы (плата должна быть 498,75). Вы должны использовать ввод для чтения строки и float() для преобразования строки в число. Не беспокойтесь об ошибке проверки ввода пользователем - предположите, что номера пользователей правильно.
hrs = input('Enter Hours:')
rph = input('Enter the rate per hour/ставку в час:')
try:
    h = float(hrs)
    r = float(rph)
    pay = 0

except:
    print('Error, please enter numeric input')
    quit() # Прекратить.
if h > 40 :
    pay = 40 * r + (h-40)*(1.5*10.5)
else:
    pay = h * r
print(pay)


 # 105
 #  15
 # 525
 #105
 #1575

 #   75
 # 15

 # 1575
 #    5
 # 7875

 # 105
 #   40
 # 420.0
