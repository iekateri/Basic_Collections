def get_input_parameters():
    """
    Получаем набор клеток

    :return: набор клеток, например: [3, 0, 6, 2, 10]
    :rtype: List[int]
    """
    cell = int(input("Количество клеток: "))
    cells = []
    for item in range(cell):
        print(f"Эффективность {item + 1} клетки : ", end="")
        cells.append(int(input()))

    return (cells)
    pass


def display_result(cells):
    """
    Выводим список клеток у которых значение меньше индекса

    :param cells: набор клеток, например: [0, 2]
    :type cells: List[int]
    """
    print("Неподходящие значения:", end="")
    for item in range(len(cells)):
        print(" ", cells[item], end="")
    pass


def select_cells(cells):
    """
    Отбираем список клеток, у которых значение меньше индекса.

    :param cells: набор клеток, например: [3, 0, 6, 2, 10]
    :type cells: List[int]

    :return: набор подходящих клеток, например: [0, 2]
    :rtype: List[int]
    """
    new_cells = []
    for item in range(len(cells)):
        if item > int(cells[item]):
            new_cells.append(cells[item])

    return (new_cells)
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    cells = get_input_parameters()  # получаем параметры
    result_cells = select_cells(cells)  # отбираем клетки
    display_result(result_cells)  # выводим результат
