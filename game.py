from field_generator import *
import copy


class Ship:
    def __init__(self, bow, horizontal, length):
        self.bow = bow
        self.horizontal = horizontal
        self.__length = length
        self.__hit = [False] * self.__length

    def shoot_at(self, tup):
        if self.horizontal:
            for i in range(self.__length):
                if (self.bow[1] + i, self.bow[0]) == tup:
                    self.__hit[i] = True
        else:
            for i in range(self.__length):
                if (self.bow[1], self.bow[0] + i) == tup:
                    self.__hit[i] = True

    def __repr__(self):
        return "*"


class Field:
    def __init__(self):
        self.__ships = generate_field()
        for i in range(len(self.__ships)):
            for j in range(len(self.__ships[i])):
                if self.__ships[i][j] == 1:
                    l = ship_size(self.__ships, (chr(j + 65), i + 1))
                    if l[1] == 1:
                        ship = Ship((i, j), True, l[0])
                        for k in range(l[0]):
                            self.__ships[i][j + k] = ship
                    elif l[0] == 1:
                        ship = Ship((i, j), True, l[1])
                        for k in range(l[1]):
                            self.__ships[i + k][j] = ship
        self.ships = self.__ships

    def shoot_at(self, tup):
        if isinstance(self.__ships[tup[0]][tup[1]], Ship):
            self.__ships[tup[0]][tup[1]].shoot_at(tup)
            self.__ships[tup[0]][tup[1]] = "X"
            return True
        elif self.__ships[tup[0]][tup[1]] == "X":
            return True
        else:
            self.__ships[tup[0]][tup[1]] = "O"
            return False

    def field_without_ships(self):
        field = copy.deepcopy(self.__ships)
        for i in range(len(field)):
            for j in range(len(field)):
                if field[i][j] == "O" or field[i][j] == "X":
                    pass
                else:
                    field[i][j] = " "
        return field_to_str(field)

    def field_with_ships(self):
        field = copy.deepcopy(self.__ships)
        for i in range(len(field)):
            for j in range(len(field[i])):
                if field[i][j] == 0:
                    field[i][j] = " "
        return field_to_str(field)


class Player:
    def __init__(self, name):
        self.__name = name

    def read_position(self):
        pos = input().split(" ")
        try:
            ver, hor = int(pos[1]) - 1, list(alpha[:10]).index(pos[0].upper())
            assert 0 <= ver < 10 and 0 <= hor < 10
        except (AssertionError, ValueError, IndexError):
            print("Wrong coordinates, enter again: ")
            return self.read_position()
        return ver, hor


class Game:
    def __init__(self, current_player=0):
        self.__field = [Field(), Field()]
        self.__players = [Player(input("Player 1, enter your name: ")),
                          Player(input("Player 2, enter your name: "))]
        self.__current_player = current_player

    def read_position(self):
        return self.__players[self.__current_player].read_position()

    def field_without_ships(self, index):
        return self.__field[index].field_without_ships()

    def field_with_ships(self, index):
        return self.__field[index].field_with_ships()

    def winner(self, player):
        if self.__field[player - 1].field_with_ships().count("X") == 20:
            return True
        return False

    def start_game(self):
        print("Game Battleship")
        while True:
            self.__current_player = 0
            print("Player {}, it`s your turn now!\n"
                  "Enter coordinates to "
                  "shoot: ".format(str(self.__current_player + 1)))
            coords = self.read_position()
            shoot = self.__field[self.__current_player].shoot_at(coords)
            while shoot:
                print("Nice, shoot again: ")
                print(
                    self.__field[self.__current_player].field_without_ships())
                coords = self.read_position()
                shoot = self.__field[self.__current_player].shoot_at(coords)
            else:
                print("Uhhh, you missed")
            print(self.__field[self.__current_player].field_without_ships())
            if self.winner(self.__current_player):
                print("Player {} WON!!! "
                      "Congratulations!".format(self.__current_player))
            self.__current_player += 1
            print("Player {}, it`s your turn now!\n"
                  "Enter coordinates to "
                  "shoot: ".format(str(self.__current_player+1)))
            coords = self.read_position()
            shoot = self.__field[self.__current_player].shoot_at(coords)
            while shoot:
                print("Nice, shoot again: ")
                print(
                    self.__field[self.__current_player].field_without_ships())
                coords = self.read_position()
                shoot = self.__field[self.__current_player].shoot_at(coords)
            else:
                print("Uhhh, you missed")
            print(self.__field[self.__current_player].field_without_ships())
            if self.winner(self.__current_player):
                print("Player {} WON!!! "
                      "Congratulations!".format(self.__current_player))
                exit()



game = Game()
game.start_game()
