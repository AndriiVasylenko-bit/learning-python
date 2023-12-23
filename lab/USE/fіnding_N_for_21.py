def process_number(N):
    mas = []
    for digit in str(N):
        mas.append(int(digit))
    digit_sum = sum(mas)

    binary_representation = bin(digit_sum)[2:]
    count_ones = binary_representation.count('1')

    if count_ones % 2 == 0:
        result = '1' + binary_representation + '00'
    else:
        result = '10' + binary_representation + '1'

    R = int(result, 2)
    return R

count = 0
for number in range(10 ** 8, 10 ** 9):  # Рассмотрение девятизначных чисел
    if process_number(number) == 21:
        count += 1

print(f"Количество N, дающее результат автомата 21,: {count}")