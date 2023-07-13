import os
import random as rnd
import time


def int_input(message, allowed_value_list):
    while True:
        raw_input = input(message)
        try:
            result = int(raw_input)
            if result in allowed_value_list:
                return result
            else:
                input('Значение за пределами допустимого. Нажмите Enter для повтора.')
                continue
        except:
            input('Не удалось распознать число. Нажмите Enter для повтора.')
            continue


def render_sticks(stick_count, stack):
    for i in range(3):
        render_string = ''
        if i == 1:
            for j in range(len(stack)):
                render_string += stack[j] + ' '  # в рендер добавляем зачеркнутые палочки из стека
            for j in range(stick_count - len(stack)):
                render_string += '/ '
        else:
            for j in range(stick_count):
                render_string += '/ '
        print(render_string)


def available_stick_count(stick_count, stack):
    available = stick_count - len(stack)
    if available >= 3:
        return 3
    else:
        return available


def cross_sticks(crossed_count, stack, current_turn, stick_count):
    available = available_stick_count(stick_count, stack)
    if crossed_count > 3 or crossed_count < 1:
        crossed_count = available
    if current_turn == 1:
        for i in range(crossed_count):
            stack.append('И')
    elif current_turn == 2:
        for i in range(crossed_count):
            stack.append('К')


def move(current_turn, stick_count, stack, hard_level):
    available = available_stick_count(stick_count, stack)
    if current_turn == 1:
        crossed_sticks = int_input('Введите количество палочек, '
                                   'которое хотите зачеркнуть (1-' +
                                    str(available) + '):', range(1, available+1))
        cross_sticks(crossed_sticks, stack, current_turn, stick_count)
    elif current_turn == 2:
        if hard_level == 1:
            crossed_sticks = rnd.randrange(1, available + 1)
            cross_sticks(crossed_sticks, stack, current_turn, stick_count)
        elif hard_level == 2:
            raw_stick_count = stick_count - 5
            quartet_count = int(raw_stick_count/4)
            first_stage_length = raw_stick_count - (quartet_count*4)
            current_quartet = int((len(stack) - first_stage_length) / 4) + 1
            crossed_sticks = 0
            if len(stack) == 0:
                if first_stage_length == 0:
                    crossed_sticks = 1
                else:
                    crossed_sticks = first_stage_length
            elif len(stack) == first_stage_length+1+(current_quartet*4):
                crossed_sticks = 1
            elif 0 < len(stack) <= first_stage_length:
                crossed_sticks = first_stage_length-len(stack)
            elif first_stage_length < len(stack) <= raw_stick_count:
                crossed_sticks = (current_quartet*4) - (len(stack)-first_stage_length)
            elif len(stack) > raw_stick_count:
                crossed_sticks = stick_count - len(stack) - 1

            cross_sticks(crossed_sticks, stack, current_turn, stick_count)
            print('Компьютер зачеркнул ' + str(crossed_sticks) + ' палочек, переход хода...')
            time.sleep(2)


def determine_first_turn():
    first_turn = rnd.randrange(1, 3)
    if first_turn == 1:
        print('Первый ход предоставляется игроку.')
        return first_turn
    else:
        print('Первый ход предоставляется компьютеру.')
        return first_turn


def choose_level():
    os.system('cls')
    choose = int_input('Выберите уровень сложности (1 - легко, 2 - сложно): ', range(1, 3))
    game(choose)


def menu():
    while True:
        os.system('cls')
        print('Главное меню. Выберите пункт: \n1. Играть \n2. Правила \n3. Выход')
        choose = int_input('Ваш ввод: ', range(1, 4))
        if choose == 1:
            choose_level()
        elif choose == 2:
            rules()
        elif choose == 3:
            os.close(0)


def rules():
    os.system('cls')
    print(
        'Игра палочки. Правила: '
        '\nВ начале игры создается игровое поле'
        '\nиз случайного количества палочек (9-20 штук).'
        '\nПосле генерации поля случайным образом '
        '\nвыбирается игрок, который будет ходить первым. '
        '\nХод – зачеркивание от 1 до 3 палочек слева направо.'
        '\nКак только игрок 1 зачеркнул нужное количество палочек, '
        '\nход переходит игроку 2 и т.д. Проигравшим считается игрок,'
        '\nкоторый зачеркнет последнюю палочку.\n'
        '\nПалочки, которые зачеркнул игрок отображаются так: \n/\nИ\n/\n'
        '\nПалочки, которые зачеркнул компьютер отображаются так: \n/\nК\n/')
    input('\nНажмите Enter для выхода в меню.\n')
    return


def game(hard_level):
    stick_count = rnd.randrange(9, 21)
    stack = []
    current_turn = determine_first_turn()
    while not len(stack) == stick_count:
        if current_turn == 1:
            print('Осталось палочек:', (stick_count - len(stack)))
            render_sticks(stick_count, stack)
        move(current_turn, stick_count, stack, hard_level)
        if current_turn == 1:
            current_turn = 2
        elif current_turn == 2:
            current_turn = 1
        os.system('cls')
    if stack[len(stack)-1] == 'И':
        print('Компьютер победил.')
    else:
        print('Игрок победил.')
    render_sticks(stick_count, stack)
    input('Нажмите Enter, чтобы выйти в меню.')
    return


menu()
