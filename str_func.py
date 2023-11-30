def str_func(value: str):

    """Функция возвращает буквы капсом"""

    return value.upper()


def capitalize_func(value: str):

    """Функция, которая делает заглавными первые буквы каждого слова"""

    return ' '.join(word.capitalize() for word in value.split())
