import os
import random as rnd


def render_sticks(stick_count, stack):
    for i in range(3):  # три ряда для рендера палочек
        render_string = ''
        if i == 1:  # если второй ряд рендера
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
        try:
            crossed_sticks = int(input('Введите количество палочек, '
                                       'которое хотите зачеркнуть (1-' +
                                       str(available) + '):'))
        except ValueError or TypeError:
            crossed_sticks = rnd.randrange(1, available + 1)
            print('Вы ввели не число, количество палочек будет'
                  ' определено случайно:', crossed_sticks)
        if crossed_sticks > available or crossed_sticks < 1:
            crossed_sticks = rnd.randrange(1, available + 1)
            print('Вы ввели слишком маленькое/большое число, количество'
                  ' палочек будет определено случайно:', crossed_sticks)
        cross_sticks(crossed_sticks, stack, current_turn, stick_count)
    elif current_turn == 2:
        if hard_level == 1:
            crossed_sticks = rnd.randrange(1, available + 1)
            cross_sticks(crossed_sticks, stack, current_turn, stick_count)
        elif hard_level == 2:
            pass


def determine_first_turn():
    first_turn = rnd.randrange(1, 3)
    if first_turn == 1:
        print('Первый ход предоставляется игроку.')
        return first_turn
    else:
        print('Первый ход предоставляется компьютеру.')
        return first_turn


def choose_level():
    final_choose = 0
    while True:
        os.system('cls')
        try:
            choose = int(input('Выберите уровень сложности (1 - легко, 2 - сложно): '))
            if choose < 1 or choose > 2:
                input('Неверный ввод, повторите попытку. Нажмите Enter.')
                continue
            else:
                final_choose = choose
                break
        except ValueError or TypeError:
            input('Неверный ввод, повторите попытку. Нажмите Enter.')
            continue
    game(final_choose)


def menu():
    while True:
        os.system('cls')
        print('Главное меню. Выберите пункт: \n1. Играть \n2. Правила \n3. Выход')
        choose = intinput()
        try:
            inp = int(input('Ваш ввод: '))
            if inp == 1:
                choose_level()
            elif inp == 2:
                rules()
            elif inp == 3:
                os.close(0)
            else:
                input('Отсутствует выбранный пункт меню. Нажмите Enter.')
        except ValueError:
            input('Ошибка ввода, повторите попытку. Нажмите Enter.')
            continue


def rules():
    os.system('cls')
    print(
        'Игра палочки. Правила: \nВ начале игры создается игровое поле\nиз случайного количества палочек (9-20 штук).')
    print('После генерации поля случайным образом \nвыбирается игрок, который будет ходить первым.')
    print(
        'Ход – зачеркивание от 1 до 3 палочек слева направо.\nКак только игрок 1 зачеркнул нужное количество палочек,')
    print('ход переходит игроку 2 и т.д. Проигравшим считается игрок,\nкоторый зачеркнет последнюю палочку.\n')
    print('Палочки, которые зачеркнул игрок отображаются так: \n/\nИ\n/\n')
    print('Палочки, которые зачеркнул компьютер отображаются так: \n/\nК\n/')
    input('\nНажмите Enter для выхода в меню.\n')
    return


def game(hard_level):
    os.system('cls')
    stick_count = rnd.randrange(9,21)
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
        else:
            input('Что-то пошло не так, выход в меню. Нажмите Enter.')
            return
        os.system('cls')
    if stack[len(stack)-1] == 'И':
        print('Компьютер победил.')
    else:
        print('Игрок победил.')
    render_sticks(stick_count, stack)
    input('Нажмите Enter, чтобы выйти в меню.')
    return


menu()