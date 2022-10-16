def get_input_parameters():
    """
    Получаем входное слово

    :return: например: abccba
    :rtype: str
    """
    return input("Введите слово: ")
    pass


def display_result(is_palindrome):
    """
    Выводим информацию является ли строка палиндромом

    :param is_palindrome: является ли палиндромом, например: True
    :type is_palindrome: bool
    """
    if is_palindrome:
        print("Слово является палиндромом")
    else:
        print("Слово не является палиндромом")
    pass


def check_palindrome(word):
    """
    Проверяем является ли слово палиндромом.

    :param word: слово, например: abccba
    :type word: str

    :return: является ли слово палиндром, например: True
    :rtype: bool
    """
    reverce_word = ""
    for num in range(len(word)):
        reverce_word += word[len(word) - 1 - num]
    if reverce_word == word:
        check = True
    else:
        check = False
    return check
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    is_palindrome = check_palindrome(word)  # является ли слово палиндромом.
    display_result(is_palindrome)  # выводим результат
