# Determination of the empty field
m = [[' ' for j in range(3)] for i in range(3)]
print("---------")
for i in range(3):
    print(f"| {m[i][0]} {m[i][1]} {m[i][2]} |")
print("---------")

player = " "

# Game logic
while True:
    n_X = 0
    n_O = 0
    n__ = 0
    try:
        if player == "X":
            player = "O"
        else:
            player = "X"
        # moving of players
        coord = input().split()
        for i in range(len(coord)):
            coord[i] = int(coord[i]) - 1
        if m[coord[0]][coord[1]] == ' ':
            m[coord[0]][coord[1]] = m[coord[0]][coord[1]].replace(' ', player)

            # the gird
            print("---------")
            for i in range(3):
                print(f"| {m[i][0]} {m[i][1]} {m[i][2]} |")
            print("---------")

            for i in range(3):
                for j in range(3):
                    if m[i][j] == "X":
                        n_X += 1
                    elif m[i][j] == 'O':
                        n_O += 1
                    else:
                        n__ += 1

            # Analyze state of gird
            if (m[0][0] == m[0][1] == m[0][2] == player) or (m[0][0] == m[1][1] == m[2][2] == player) or (
                    m[1][0] == m[1][1] == m[1][2] == player) or (m[2][0] == m[2][1] == m[2][2] == player):
                print(f'{player} wins')
                break
            elif (m[0][2] == m[1][1] == m[2][0] == player) or (m[0][0] == m[1][0] == m[2][0] == player) or (
                    m[0][1] == m[1][1] == m[2][1] == player) or (m[0][2] == m[1][2] == m[2][2] == player):
                print(f'{player} wins')
                break
            elif n__ == 0:
                print('Draw')
                break
            else:
                continue
        else:
            print('This cell is occupied! Choose another one!')
            if player == "X":
                player = "O"
            else:
                player = "X"
    except ValueError:
        print('You should enter numbers!')
        if player == "X":
            player = "O"
        else:
            player = "X"
        continue
    except IndexError:
        print('Coordinates should be from 1 to 3!')
        if player == "X":
            player = "O"
        else:
            player = "X"
        continue
