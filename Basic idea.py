options = ['1', '2', '3', '4', '5', '6', '7']
board = [['*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*'], ]
board_height = 7
board_length = 7


def valid_user(user):
    if len(user) == 1:
        return True


def user_one():
    u1 = input('Player 1, please choose an integer or letter to represent your player: ')
    while not valid_user(u1):
        print('Your username must be 1 character long!')
        u1 = input('Player 1, please choose an integer or letter to represent your player: ')
    return u1


one = user_one()


def valid_user_2(user1, user2):
    if user2 == user1:
        print('That username is already taken!')
        return False
    else:
        return True


def user_two():
    u2 = input('Player 2, please choose an integer or letter to represent your player: ')
    while (not valid_user(u2)) or (not valid_user_2(one, u2)):
        print('Your username must be 1 character long!')
        u2 = input('Player 2, please choose an integer or letter to represent your player: ')
    return u2


two = user_two()

letter = None
turns = 0


def print_board():
    print('  '.join(options))
    print('\n'.join(map('  '.join, board)))
    print('\n')


def checkt(turns):
    turns += 1


def choose_spot(turns):
    try:
        s = int(input('Choose your spot: '))
        print('\n')
        x = 6
        while board[x][s - 1] != '*':
            x -= 1
        board[x][s - 1] = letter
        return True
    except IndexError:
        print('That spot is not an option. Try again.')
    except ValueError:
        print('That spot is not an option. Try again.')


def vert_win(letter):
    for x in range(6, -1, -1):
        for y in range(7):
            try:
                if board[x][y] == board[x - 1][y] == board[x - 2][y] == board[x - 3][y] == letter:
                    return True
                else:
                    continue
            except IndexError:
                continue


def horiz_win(letter):
    for x in range(6, -1, -1):
        for y in range(7):
            try:
                if board[x][y] == board[x][y + 1] == board[x][y + 2] == board[x][y + 3] == letter:
                    return True
                else:
                    continue
            except IndexError:
                continue


def diag_win(letter):
    for x in range(6, -1, -1):
        for y in range(7):
            try:
                if board[x][y] == board[x - 1][y + 1] == board[x - 2][y + 2] == board[x - 3][y + 3] == letter:
                    return True
                elif board[x][y] == board[x - 1][y - 1] == board[x - 2][y - 2] == board[x - 3][y - 3] == letter:
                    return True
            except IndexError:
                continue


while True:
    print_board()
    if vert_win(letter):
        print(letter, 'won vertically! Congratulations')
        break
    elif horiz_win(letter):
        print(letter, 'won horizontally! Congratulations')
        break
    elif diag_win(letter):
        print(letter, 'won diagonally! Congratulations')
        break
    if turns % 2 == 0:
        letter = one
    else:
        letter = two
    if choose_spot(turns):
        turns += 1