# Row - i
# Column - j

for row in range(7):
    for column in range(34):
        # For T
        if row == 0 and column <= 5:
            print("*", end=" ")
        elif column == 2 and (row == 1 or row == 2 or row == 3 or row == 4 or row == 5 or row == 6):
            print("*", end=" ")

        # For R - From Column 5
        elif row == 0 and column > 5 and column != 9 and column < 9:
            print("*", end=" ")
        elif row == 1 and (column == 5 or column == 9):
            print("*", end=" ")
        elif row == 2 and (column == 5 or column == 9):
            print("*", end=" ")
        elif row == 3 and (column >= 5 and column < 9):
            print("*", end=" ")
        elif row == 4 and (column == 5 or column == 7):
            print("*", end=" ")
        elif row == 5 and (column == 5 or column == 8):
            print("*", end=" ")
        elif row == 6 and (column == 5 or column == 9):
            print("*", end=" ")

        # For I - From Column 10
        elif row == 0 and (column <= 14 and column >= 10):
            print("*", end=" ")
        elif (row == 1 or row == 2 or row == 3 or row == 4 or row == 5) and column == 12:
            print("*", end=" ")
        elif row == 6 and (column >= 10 and column <= 14):
            print("*", end=" ")

        # For S - From Column 15
        elif row == 0 and column > 15 and column != 18 and column < 18:
            print("*", end=" ")
        elif row == 1 and column == 15:
            print("*", end=" ")
        elif row == 2 and column == 15:
            print("*", end=" ")
        elif row == 3 and (column == 16 or column == 17):
            print("*", end=" ")
        elif row == 4 and column == 18:
            print("*", end=" ")
        elif row == 5 and column == 18:
            print("*", end=" ")
        elif row == 6 and (column == 16 or column == 17):
            print("*", end=" ")

        # For H - From Column 19
        elif row == 0 and (column == 19 or column == 22):
            print("*", end=" ")
        elif row == 3 and (column >= 19 and column <= 22):
            print("*", end=" ")
        elif (row == 1 or row == 2 or row == 4 or row == 5 or row == 6) and (column == 19 or column == 22):
            print("*", end=" ")

        # For A - From Column 23
        elif column == 23 and row != 0:
            print("*", end=" ")
        elif column == 24 and (row == 0 or row == 3):
            print("*", end=" ")
        elif column == 25 and (row == 0 or row == 3):
            print("*", end=" ")
        elif column == 26 and (row == 0 or row == 3):
            print("*", end=" ")
        elif column == 27 and row != 0:
            print("*", end=" ")

        # For N - From Column 28:
        elif (column == 28 or column == 33) and row == 0:
            print("*", end=" ")
        elif row == 1 and (column == 28 or column == 29 or column == 33):
            print("*", end=" ")
        elif row == 2 and (column == 28 or column == 30 or column == 33):
            print("*", end=" ")
        elif row == 3 and (column == 28 or column == 31 or column == 33):
            print("*", end=" ")
        elif row == 4 and (column == 28 or column == 32 or column == 33):
            print("*", end=" ")
        elif row == 5 and (column == 28 or column == 33):
            print("*", end=" ")
        elif row == 6 and (column == 28 or column == 33):
            print("*", end=" ")
        else:
            print(end="  ")

    print()
