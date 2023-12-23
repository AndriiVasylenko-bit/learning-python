def process_number(N):
    # Step 1: Найти сумму цифр N
    digit_sum = sum(int(digit) for digit in str(N))
    # Step 2: Перевести сумму в двоичный файл
    binary_representation = bin(digit_sum)[2:]

    # Step 3: Проверить, является ли число единиц в двоичном представлении чётным или нечётным
    count_ones = binary_representation.count('1')

    if count_ones % 2 == 0:
        # Если число одинаковых, добавьте 1 слева и 00 справа
        result = '1' + binary_representation + '00'
    else:
        # Если число элементов нечётно, добавьте '10' слева и '1' справа
        result = '10' + binary_representation + '1'

    # Интерпретировать полученное двоичное представление как десятичное число R
    R = int(result, 2)
    return R

# Использование примеров
N = 123456789
result_R = process_number(N)
print(f"Для N = {N} результат R = {result_R}")
