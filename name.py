for row in range(12):
    for column in range(5):
        if column == 0:
            print("*", end=" ")
        elif column == 1 and row == 1:
            print("*", end=" ")
        elif column == 2 and row == 2:
            print("*", end=" ")
        elif column == 1 and row == 3:
            print("U", end=" ")
        elif column == 1 and row == 7:
            print("O", end=" ")
        elif column == 3 and row == 3:
            print("*", end=" ")
        elif row == 4 or row == 8:
            print("*", end=" ")
        elif row == 5 and column == 1:
            print("*", end=" ")
        elif row == 6 and column == 2:
            print("*", end=" ")
        elif row == 7 and column == 3:
            print("*", end=" ")
        else:
            print(end="  ")
    print()
