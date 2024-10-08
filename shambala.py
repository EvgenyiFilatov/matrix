"""Шаман племени «Тумба-Юмба» обладает особым даром – он умеет отгонять беду
от посевов племени. Но для успешного камлания он должен в день начала посевов
правильно сложить особенную фигуру, называемую Шамбалой, чтобы боги погоды были
благосклонны к жителям племени. Как строится Шамбала посмотрите в прилагаемых к
задаче примерах.
В задаче нужно вывести на экран в символическом виде концентрические круги
символами ‘X’ и пробелами, количество которых зависят от номера N текущего дня.
На вход подаётся одна строка с числом N [1, 30].
На выход нужно подать несколько строк с изображением шамбалы."""


def print_shambala(N):
    size = 2 * N - 1  # Определяем размер квадратной области
    center = N - 1  # Центр квадрата

    for y in range(size):     # Проход по строкам
        line = ""
        for x in range(size):  # Проход по столбцам
            # Вычисляем расстояние до центра
            distance = max(abs(center - x), abs(center - y))

            if distance % 2 == 0 and N % 2 == 0:
                line += ' '
            elif distance % 2 != 0 and N % 2 == 0:
                line += 'X'
            elif distance % 2 == 0 and N % 2 != 0:
                line += 'X'
            elif distance % 2 != 0 and N % 2 != 0:
                line += ' '
        print(line)  # Печатаем полученную строку


# Чтение входного значения
N = int(input())
print_shambala(N)
