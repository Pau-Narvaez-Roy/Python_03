#!/usr/bin/env python3
import math


def get_player_pos() -> tuple:
    while True:
        str = input("Enter new coordinates as floats in formats 'x,y,z': ")
        list = []
        try:
            if len(str.split(',')) != 3:
                raise IndexError
            for i in range(0, 3):
                index_error = i
                list.append(round(float(str.split(',')[i]), 1))
            break
        except IndexError:
            print("Invalid syntax")
        except ValueError:
            print(f"Error on parameter '{str.split(',')[index_error]}':",
                  "could not convert string to float:",
                  f"'{str.split(',')[index_error]}'")
    tuple = [list[0], list[1], list[2]]
    return tuple


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    tuple_1 = get_player_pos()
    print(f"Got a first tuple: ({tuple_1[0]}, {tuple_1[1]}, {tuple_1[2]})")
    print(f"It includes: X={tuple_1[0]},  Y={tuple_1[1]},  Z={tuple_1[2]}")
    x_sq2 = tuple_1[0] ** 2
    y_sq2 = tuple_1[1] ** 2
    z_sq2 = tuple_1[2] ** 2
    res = round(math.sqrt(x_sq2 + y_sq2 + z_sq2), 4)
    print(f"Distance to center: {res}\n")
    print("Get a second set of coordinates")
    tuple_2 = get_player_pos()
    x_sq2 = tuple_1[0] ** 2 - (2 * tuple_1[0] * tuple_2[0]) + tuple_2[0] ** 2
    y_sq2 = tuple_1[1] ** 2 - (2 * tuple_1[1] * tuple_2[1]) + tuple_2[1] ** 2
    z_sq2 = tuple_1[2] ** 2 - (2 * tuple_1[2] * tuple_2[2]) + tuple_2[2] ** 2
    res = round(math.sqrt(x_sq2 + y_sq2 + z_sq2), 4)
    print(f"Distance between the 2 sets of coordinates: {res}")
