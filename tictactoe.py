def Print_Table(line):
    print("---------")
    for k in range(0, 7, 3):
        print(f"| {line[k]} {line[k + 1]} {line[k + 2]} |")
    print("---------")


def Check_Status(array):
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

    if wins_x:
        return "XW"
    elif wins_o:
        return "OW"
    if ' ' not in array:
        return "DW"


array_main = [x for x in '         ']
Print_Table(array_main)
while True:
    if Check_Status(array_main) == "XW":
        print("X wins")
        break
    elif Check_Status(array_main) == "OW":
        print("O wins")
        break
    elif Check_Status(array_main) == "DW":
        print("Draw")
        break
    coordinates = input("Enter the coordinates: ")
    if coordinates.isalpha():
        print("You should enter numbers!")
    else:
        array_coordinates = coordinates.split()
        if int(array_coordinates[0]) > 3 or int(array_coordinates[1]) > 3:
            print("Coordinates should be from 1 to 3!")
        else:
            if int(array_coordinates[0]) == 1 and int(array_coordinates[1]) == 3:
                if array_main[0] != ' ':
                    print("This cell is occupied! Choose another one!")
                else:
                    array_main[0] = 'X'
                    Print_Table(array_main)
            elif int(array_coordinates[0]) == 2 and int(array_coordinates[1]) == 3:
                if array_main[1] != ' ':
                    print("This cell is occupied! Choose another one!")
                else:
                    array_main[1] = 'X'
                    Print_Table(array_main)
            elif int(array_coordinates[0]) == 3 and int(array_coordinates[1]) == 3:
                if array_main[2] != ' ':
                    print("This cell is occupied! Choose another one!")
                else:
                    array_main[2] = 'X'
                    Print_Table(array_main)
            elif int(array_coordinates[0]) == 1 and int(array_coordinates[1]) == 2:
                if array_main[3] != ' ':
                    print("This cell is occupied! Choose another one!")
                else:
                    array_main[3] = 'X'
                    Print_Table(array_main)
            elif int(array_coordinates[0]) == 2 and int(array_coordinates[1]) == 2:
                if array_main[4] != ' ':
                    print("This cell is occupied! Choose another one!")
                else:
                    array_main[4] = 'X'
                    Print_Table(array_main)
            elif int(array_coordinates[0]) == 3 and int(array_coordinates[1]) == 2:
                if array_main[5] != ' ':
                    print("This cell is occupied! Choose another one!")
                else:
                    array_main[5] = 'X'
                    Print_Table(array_main)
            elif int(array_coordinates[0]) == 1 and int(array_coordinates[1]) == 1:
                if array_main[6] != ' ':
                    print("This cell is occupied! Choose another one!")
                else:
                    array_main[6] = 'X'
                    Print_Table(array_main)
            elif int(array_coordinates[0]) == 2 and int(array_coordinates[1]) == 1:
                if array_main[7] != ' ':
                    print("This cell is occupied! Choose another one!")
                else:
                    array_main[7] = 'X'
                    Print_Table(array_main)
            elif int(array_coordinates[0]) == 3 and int(array_coordinates[1]) == 1:
                if array_main[8] != ' ':
                    print("This cell is occupied! Choose another one!")
                else:
                    array_main[8] = 'X'
                    Print_Table(array_main)
