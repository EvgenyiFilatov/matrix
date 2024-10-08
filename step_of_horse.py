"""Напишите программу, которая будет проверять правильность хода Конём.
На вход подаётся строка – это шахматная запись одного хода - начальной позиции
фигуры и конечной позиции, например, так: D5-C7.
На выход нужно вывести результат анализа записи хода: YES - если указанный ход
верный, NO - если такой ход не по правилам, указанным для Коня.
Гарантируется, что запись хода будет состоять из 5-ти символов, в середине
будет «дефис», буквы и цифры будут расположены на правильных местах и в
разрешённом диапазоне для шахматной доски."""


def is_knight_move(start, end):
    # Вычисляем разницы координат
    col_diff = abs(ord(end[0]) - ord(start[0]))
    row_diff = abs(int(end[1]) - int(start[1]))

    # Проверяем, соответствует ли ход правилам коня
    return ((col_diff == 2 and row_diff == 1) or
            (col_diff == 1 and row_diff == 2))


# Чтение входной строки
move = str(input())
start_position, end_position = move.split('-')

# Проверяем правильность хода
if is_knight_move(start_position, end_position):
    print("YES")
else:
    print("NO")
