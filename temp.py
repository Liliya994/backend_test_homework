from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')

print(message)


def calculateSquareRoot(Number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number: float) -> float:
    """Проверяет на отрицательные значения."""
    if your_number <= 0:
        return 0
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет:{calculateSquareRoot(your_number)}')


calc(25.5)
