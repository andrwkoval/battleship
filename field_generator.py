from string import ascii_uppercase
from random import randint


def read_field(filename):
    with open(filename, "r", encoding="utf-8", errors="ignore") as file_ships:
        field = [[0] * 10 for i in range(10)]
        data = file_ships.readlines()
        for i in range(10):
            for j in range(len(data[i][:10])):
                if data[i][j] == "*":
                    field[i][j] = 1
    return field


def has_ship(field, coords):
    lets = list(ascii_uppercase[:10])
    return field[coords[1] - 1][lets.index(coords[0].upper())] == 1


def ship_size(field, coords):
    lets = list(ascii_uppercase[:10])

    if not has_ship(field, coords):
        return (0, 0)

    ver, hor = coords[1] - 1, lets.index(coords[0].upper())
    horizontal, vertical = 1, 1

    step = 1
    while ver - step >= 0 and field[ver - step][hor] == 1:
        vertical, step = vertical + 1, step + 1

    step = 1
    while ver + step < 10 and field[ver + step][hor] == 1:
        vertical, step = vertical + 1, step + 1

    step = 1
    while hor - step >= 0 and field[ver][hor - step] == 1:
        horizontal, step = horizontal + 1, step + 1

    step = 1
    while hor + step < 10 and field[ver][hor + step] == 1:
        horizontal, step = horizontal + 1, step + 1

    return (horizontal, vertical)


def is_valid(field):
    lets = list(ascii_uppercase[:10])
    ships = [4]*4 + [3]*6 + [2]*6 + [1]*4

    if len([1 for i in field for j in i if j == 1]) != 20:
        return False

    if (field[0][1] and field[1][0]) or (field[0][9] and field[1][9]) or \
            (field[8][0] and field[9][1]) or (field[8][9] and field[9][8]):
        return False

    for i in range(len(field)):
        for j in range(len(field[i])):
            if valid_location(field, (lets[i], j+1)):
                a = ship_size(field, (lets[i], j+1))
                try:
                    if a[0] >= a[1] and a[1] == 1:
                        ships.remove(a[0])
                    elif a[0] <= a[1] and a[0] == 1:
                        ships.remove(a[1])
                except ValueError:
                    return False
    if ships:
        return False
    return True


def valid_location(field, coords):
    if has_ship(field, coords):
        lets = list(ascii_uppercase[:10])
        ver, hor = coords[1] - 1, lets.index(coords[0].upper())
        if (1<=ver<9 and 1<=hor<9) and \
            (field[ver - 1][hor - 1] == 1 or field[ver - 1][hor + 1] == 1 or
                field[ver + 1][hor - 1] == 1 or field[ver + 1][hor + 1]):
            return False
        return True


