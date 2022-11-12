# Создайте программу для игры в ""Крестики-нолики"".
#
board = list(range(1, 10))


def draw_board(board):
    print('_' * 13)
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[ 2+ i * 3], '|')
        print('_' * 13)


def take_input(token):
    valid = False
    while not valid:
        player_answer = input('Выбирите куда поставить ' + token + '?')
        try:
            player_answer = int(player_answer)
        except:
            print("Ошибка !!! Проверти ввели ли вы иминно число")
            continue
        if player_answer <= 9 and player_answer >= 1:
            if (str(board[player_answer - 1]) not in "XO"):
                board[player_answer - 1] = token
                valid = True
            else:
                print('Данная клетка занята фигурой')
        else:
            print('Ошибка ввода,введите число от 1 до 9')


def chek_win(board):
    win_coord = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7),(1,4,7),(2,5,8),(3,6,9))
    for each in win_coord:
      if board[each[0]] == board[each[1]] == board[each[2]]:
         return board[each[0]]
    return False


def main(board):
    count = 0
    win = False
    while not win:
        draw_board(board)
        if count % 2 == 0:
            take_input('X')
        else:
         take_input("O")
        count+=1
        if count>4:
            tmp = chek_win(board)
            if tmp:
                print(tmp,'Выйграл')
                win = True
                break
            if count == 9 :
                print('Ничья')
                break
    draw_board(board)
main(board)

