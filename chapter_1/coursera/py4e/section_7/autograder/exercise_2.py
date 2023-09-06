# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the amount() function or a variable named amount in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# 7.2 Напишіть програму, яка запитує ім'я файлу, потім відкриває цей файл і читає через файл, шукаючи рядки форми:
# X-DSPAM-впевненість: 0.8475
# Підрахуйте ці рядки і витягніть значення з плаваючою комою з кожної з ліній і обчисліть середнє значення цих значень і отримайте вивід, як показано нижче. Не використовуйте функцію amount () або змінну з назвою amount у вашому рішенні.
# Ви можете завантажити дані зразка в http://www.py4e.com/code3/mbox-short.txt, коли ви тестуєте нижче введіть mbox-short.txt як ім'я файлу.



# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
amount = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    ipos = line.find(":")
    line = float(line[ipos+1:].rstrip())
    count += 1
    amount += line
amount = amount / count
print('Average spam confidence:', amount)
