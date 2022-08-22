def privetstvie():
    print("-------------------")
    print("  Логическая игра  ")
    print("      между        ")
    print("  двумя противниками  ")
    print("  крестики и нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")

pole = [[" "] * 3 for i in range(3)]

def kartinka():
    print(f" 0 1 2")
    print(f"0 {pole[0][0]} {pole[0][1]} {pole[0][2]}")
    print(f"1 {pole[1][0]} {pole[1][1]} {pole[1][2]}")
    print(f"2 {pole[2][0]} {pole[2][1]} {pole[2][2]}")


def ask():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y