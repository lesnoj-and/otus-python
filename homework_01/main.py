"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*num: int) -> list:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [i ** 2 for i in num ]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(num):
    prime = num > 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3)
    i = 5
    d = 2
    while prime and i * i <= num:
        prime = num % i != 0
        i += d
        d = 6 - d 
    return prime


def filter_numbers(num: int, key: str) -> list:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if key == ODD:
        return [i for i in num if i % 2 != 0]
    if key == EVEN:
        return [i for i in num if i % 2 == 0]
    if key == PRIME:
        return [i for i in num if is_prime(i)]
