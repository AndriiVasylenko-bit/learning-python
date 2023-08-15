# # Get the name of the file and open it
# name = intput('Enter file:') # Получаем путь к файлу
# handle = open(name, 'r') # Открываем файл для чтения
#
# # Count word frequency/частота (histograv)
# counts = dict() # Состовляет словарь {key, value}
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word,0) + 1
#
# # Find the most common word
# # Находить самое распространенное слово
# bigcount = None
# bigword = None
# for word,counts in counts.items():
#         if bigcount is None or count > bigcount:
#             bigword = word
#             bigcount = counts
#
# # All done
# # Все готово
# print(bigword, bigcount)

# Convert elevator floors
# Конвертировать этажи лифта
inp = input('Europe floor?')
usf = int(inp) + 1
print('Us floor', usf)