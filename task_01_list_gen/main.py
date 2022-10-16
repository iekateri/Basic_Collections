def get_input_parameters():
    """
    Получаем N
    :return: N, например: 14
    :rtype: int
"""
    number_n = int(input('Введите число: '))
    return(number_n)


def display_result(odd_numbers):
    """
    Выводим список нечётных чисел
    :param odd_numbers: список нечётных чисел, например: [1, 3, 5, 7, 9, 11, 13]
    :type odd_numbers: List[int]
"""
    print(odd_numbers)
    pass


def get_odd_numbers(number):
    """
    Получаем отсортированный по возрастанию список
    нечётных чисел от 1 до number.
    :param number: до какого числа нужно рассчитать, например: 14
    :type number: int
    :return: список нечётных чисел, например: [1, 3, 5, 7, 9, 11, 13]
    :rtype: List[int]
 """
    count = 0
    list = []
    for odd_numbers in range(1, number + 1, 2):
        list.append(odd_numbers)
        count += 1
    return(list)
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    number = get_input_parameters()  # получаем параметры
    odd_numbers = get_odd_numbers(number)  # получаем нечётные числа
    display_result(odd_numbers)  # выводим результат