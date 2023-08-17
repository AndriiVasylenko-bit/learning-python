# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# З.З Напишите программу, чтобы запросить оценку в диапазоне от 0,0 до 1,0. Если оценка вне диапазона, выведите ошибку. Если балл находится между 0,0 и 1,0, выведите ранг, используя следующую таблицу:
# Score Grade/Оценка
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
# Если пользователь вводит значение вне диапазона, выведите подходящее сообщение об ошибке и выйдите. Для теста введите оценку 0,85.

score = input("Enter Score:")
score = float(score)
if score >= 0.9 :
    print("A")
elif score >= 0.8 :
    print("B")
elif score >= 0.7 :
    print("C")
elif score >= 6.0 :
    print("D")
elif score < 6.0 :
    print("F")
else:
    print("Uncorected input")