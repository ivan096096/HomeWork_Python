# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом"
from random import *

message = ['твоя очередь', 'да бери уже', 'бери больше', 'не корову проигрываешь',
           'бери быстрее', 'да харош, так долго думать уже']
def player_vs_player():
 candies_total = 2021
 max_take = 28
 count = 0
 player_1 = input('\nКак тебя зовут?: ')
 player_2 = input('\nА твоего соперника?: ')

# def oneMation():
 ger =  ('Ввозьмите конфеты ',randint(0,28))
 ger2 =  ('Ввозьмите конфеты ',randint(0,28))
 if ger > ger2:
  print('В жеребьёвке выйграл  первый игрок  :'+ player_1)
 else:
  print('В жеребьёвке выйграл  второй игрок  :  '+ player_2)

 while candies_total > 0:
        if count == 0:
            step = int(input(f'\n{choice(message)} {player_1} = '))
            if step > candies_total or step > max_take:
                step = int(input(
                    f'\nНе жадничай можно взять только {max_take} конфет {player_1}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nна кону еще {candies_total}')
            count = 1
        else:
            print('Все кончились конфетки')

        if count == 1:
            step = int(input(f'\n{choice(message)}, {player_2} '))
            if step > candies_total or step > max_take:
                step = int(input(
                    f'\nНе жадничай можно взять только {max_take} конфет {player_2}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nна кону еще {candies_total}')
            count = 0
        else:
            print(f'{player_1},{player_2}, кончились конфетки')

 if count == 1:
        print(f'{player_2} ПОБЕДИЛ')
 if count == 0:
        print(f'{player_1} ПОБЕДИЛ')
