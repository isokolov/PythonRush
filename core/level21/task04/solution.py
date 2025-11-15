def calculate_and_report(input_file, output_file):
    # Открываем входной файл для чтения
    with open(input_file, 'r') as input_file:
        numbers = input_file.read().split('\n')

    # Вычисляем сумму чисел в списке numbers
    try:
        num_int = [int(el) for el in numbers]
    except Exception as e:
        num_int = [0]

    total_sum = sum(num_int)

    # Вычисляем среднее значение; если список пустой, устанавливаем среднее равным 0
    avg = 0
    if len(numbers) ==0:
        avg = 0
    else:
        avg = total_sum / len(numbers)
    res_str = f"Сумма: {total_sum}, Среднее: {avg}"

    # Открываем выходной файл для записи отчета
    with open(output_file, 'w') as output_file:
        output_file.write(res_str)


# Запускаем функцию с заданными именами входного и выходного файлов
calculate_and_report('data.txt', 'report.txt')
