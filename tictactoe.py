def Print_Table(line):
    array = list(line)
    print("---------")
    for k in range(0, 7, 3):
        print(f"| {array[k]} {array[k + 1]} {array[k + 2]} |")
    print("---------")


def Check_Status(line):
    empty_cells = line.count('_')
    count_x = line.count('X')
    count_o = line.count('O')
    array = list(line)
    wins_x = False
    wins_o = False
    if ((array[0] == 'O' and array[1] == 'O' and array[2] == 'O')
            or (array[3] == 'O' and array[4] == 'O' and array[5] == 'O')
            or (array[6] == 'O' and array[7] == 'O' and array[8] == 'O')
            or (array[0] == 'O' and array[3] == 'O' and array[6] == 'O')
            or (array[1] == 'O' and array[4] == 'O' and array[7] == 'O')
            or (array[2] == 'O' and array[5] == 'O' and array[8] == 'O')
            or (array[0] == 'O' and array[4] == 'O' and array[8] == 'O')
            or (array[6] == 'O' and array[4] == 'O' and array[2] == 'O')):
        wins_o = True
    if ((array[0] == 'X' and array[1] == 'X' and array[2] == 'X')
            or (array[3] == 'X' and array[4] == 'X' and array[5] == 'X')
            or (array[6] == 'X' and array[7] == 'X' and array[8] == 'X')
            or (array[0] == 'X' and array[3] == 'X' and array[6] == 'X')
            or (array[1] == 'X' and array[4] == 'X' and array[7] == 'X')
            or (array[2] == 'X' and array[5] == 'X' and array[8] == 'X')
            or (array[0] == 'X' and array[4] == 'X' and array[8] == 'X')
            or (array[6] == 'X' and array[4] == 'X' and array[2] == 'X')):
        wins_x = True

    if wins_x and wins_o or abs(count_o - count_x) > 1:
        print("Impossible")
    elif wins_x:
        print("X wins")
    elif wins_o:
        print("O wins")
    elif empty_cells > 0:
        print("Game not finished")
    else:
        print("Draw")


cells = input("Enter cells: ")
Print_Table(cells)
Check_Status(cells)
