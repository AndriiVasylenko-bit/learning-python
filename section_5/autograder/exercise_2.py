# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
# 5.2 Написать программу, которая неоднократно запрашивает у пользователя целые числа, пока пользователь не введет 'готово'. После того, как будет введено 'готово', распечатайте самые большие и малые числа. Если пользователь вводит что-либо, кроме действительного номера, поймать его с помощью попытки/кроме того, и отправить соответствующее сообщение и игнорировать номер. Введите 7, 2, боб, 10, и 4 и соответствовать выходу ниже.

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        if largest is None or smallest is None:
            largest = num
            smallest = num
        if largest < num:
            largest = num
        if smallest > num:
            smallest = num
    except:
        print('Invalid input')
print("Maximum is", largest)
print("Minimum is", smallest)

