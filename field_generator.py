from string import ascii_uppercase as alpha
import random as rd


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
    return field[coords[1] - 1][list(alpha[:10]).index(coords[0].upper())] == 1


def ship_size(field, coords):
    if not has_ship(field, coords):
        return (0, 0)

    ver, hor = coords[1] - 1, list(alpha[:10]).index(coords[0].upper())
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
    lets = list(alpha[:10])
    ships = [4] * 4 + [3] * 6 + [2] * 6 + [1] * 4

    if len([1 for i in field for j in i if j == 1]) != 20:
        return False

    if (field[0][1] and field[1][0]) or (field[0][8] and field[1][9]) or \
            (field[8][0] and field[9][1]) or (field[8][9] and field[9][8]):
        return False

    for i in range(len(field)):
        for j in range(len(field[i])):
            if has_ship(field, (lets[j], i + 1)) and \
                    valid_location(field, (lets[j], i + 1)):
                a = ship_size(field, (lets[j], i + 1))
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


def valid_location(data, coords):
    lets = list(alpha[:10])
    y, x = coords[1] - 1, lets.index(coords[0].upper())
    if (0 < y < 9 and 0 < x < 9) and \
            (data[y - 1][x - 1] or data[y - 1][x + 1] or
             data[y + 1][x - 1] or data[y + 1][x + 1]):
        return False
    return True


def generate_field():
    field = [[0] * 10 for i in range(10)]
    ships = [1] * 4 + [2] * 3 + [3] * 2 + [4]
    while ships:
        ver, hor = rd.randint(ships[-1] - 1, 9), rd.randint(ships[-1] - 1, 9)
        if rd.randint(0, 1):
            for i in range(ships[-1]):
                pointer = False
                if not has_ship(field, (alpha[hor], ver + 1)) and \
                        valid_location(field, (alpha[hor], ver + 1)):
                    pointer = True
                ver -= 1
                if not pointer:
                    break
            if not pointer:
                continue
            ver += ships[-1]
            for i in range(ships[-1]):
                field[ver][hor] = 1
                ver -= 1
        else:
            for i in range(ships[-1]):
                pointer = False
                if not has_ship(field, (alpha[hor], ver + 1)) and \
                        valid_location(field, (alpha[hor], ver + 1)):
                    pointer = True
                hor -= 1
                if not pointer:
                    break
            if not pointer:
                continue
            hor += ships[-1]
            for i in range(ships[-1]):
                field[ver][hor] = 1
                hor -= 1
        ships.pop()
    if is_valid(field):
        return field
    return generate_field()


def field_to_str(field):
    str_field = "    " + "  ".join(list(alpha[:10])) + "\n"
    for i, j in enumerate(field):
        if i < 9:
            str_field += str(i + 1) + " | " + "| ".join(map(str, j))\
                         + "|" + "\n"
        else:
            str_field += str(i + 1) + "| " + "| ".join(map(str, j))\
                         + "|" + "\n"
    return str_field
