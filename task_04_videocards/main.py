def get_input_parameters():
    """
    Получаем список видеокарт

    :return: набор видеокарт, например: [3070, 2060, 3090, 3070, 3090]
    :rtype: List[int]
    """
    video_card = int(input("Кол-во видеокарт: "))
    video_cards = []

    for item in range(video_card):
        print(f"{item + 1} Видеокарта: ", end="")
        video_cards.append(int(input()))

    return(video_cards)
    pass


def display_result(old_video_cards, new_video_cards):
    """
    Выводим список оставшихся видеокарт

    :param old_video_cards: старый набор видеокарт, например: [3070, 2060, 3090, 3070, 3090]
    :type old_video_cards: List[int]
    :param new_video_cards: новый набор видеокарт, например: [3070, 2060, 3070]
    :type new_video_cards: List[int]
    """
    print("\nСтарый список видеокарт: ", old_video_cards[0], end="")
    for item in range(1, len(old_video_cards)):
        print(", ", old_video_cards[item], end="")

    print("\nНовый список видеокарт: ", new_video_cards[0], end="")
    for item in range(1, len(new_video_cards)):
        print(", ", new_video_cards[item], end="")
    pass


def select_video_cards(video_cards):
    """
    Удаляем из списка видеокарт наибольшие элементы.

    :param video_cards: набор видеокарт, например: [3070, 2060, 3090, 3070, 3090]
    :type video_cards: List[int]

    :return: набор оставшихся видеокарт, например: [3070, 2060, 3070]
    :rtype: List[int]
    """
    maximum = 0

    for item in range(len(video_cards)):
        if video_cards[item] > maximum:
            maximum = video_cards[item]

    new_list = []
    for item in range(len(video_cards)):
        if video_cards[item] < maximum:
            new_list.append(video_cards[item])

    return (new_list)
    pass


if __name__ == '__main__':
    video_cards = get_input_parameters()  # получаем параметры
    result_video_cards = select_video_cards(video_cards)  # удаляет наибольшие элементы.
    display_result(video_cards, result_video_cards)  # выводим результат
