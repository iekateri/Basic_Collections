def get_input_parameters():
    """
    Получаем неотсортированный список чисел

    :return: неотсортированный список чисел, например: [1, 4, -3, 0, 10]
    :rtype: List[int]
    """
    # TODO: в этой функции пишем весь необходимый код для
    #  получения входных параметров.
    #  Логику расчётов тут не программируем
    pass


def display_result(sorted_list):
    """
    Выводим отсортированный список

    :param sorted_list: отсортированный список, например: [-3, 0, 1, 4, 10]
    :type sorted_list: List[int]
    """
    # TODO: в этой функции пишем весь необходимый код
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем
    pass


def sort_list(original_list):
    """
    Сортируем список

    :param original_list: Исходный список: [1, 4, -3, 0, 10]
    :type original_list: List[int]

    :return: отсортированный, например: [-3, 0, 1, 4, 10]
    :rtype: List[int]
    """
    # TODO: в этой функции пишем логику сортировки списка.
    #  print'ов и input'ов тут не должно быть.
    #  Функция на вход принимает ранее полученные данные
    #  (из функции get_input_parameters).
    #  Функция на выход отдаёт результат необходимый для отображения работы программы,
    #  который будет передан в функцию display_result.
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    original_list = get_input_parameters()  # получаем параметры
    sorted_list = sort_list(original_list)  # сортируем список.
    display_result(sorted_list)  # выводим результат
