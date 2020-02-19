import random


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


def game_core_v2(number, count=0, limit_min=1, limit_max=100):

    #  Сначала устанавливаем диапазон поиска, если диапазон нельзя разделить на два ( в нем нет целых чисел),
    #  проверяем обе его границы, иначе проверяем число на его середине в зависимости от того, больше оно
    #  или меньше нужного. Если число на середине больше нужного, вызываем функцию рекурсивно от нижней
    #  половины диапазона, иначе - от верхней половины.
    #  Функция принимает загаданное число, текущее число попыток и границы диапазона,
    #  и возвращает число попыток угадывания.

    gap = limit_max - limit_min
    if gap == 1:
        count += 1
        predict = limit_min
        if number == predict:
            return count  # возврат, если угадали
        else:
            predict = limit_max
            if number == predict:
                return count  # возврат, если угадали
            else:
                print('Error in guessing')
                return 1000  # аварийный возврат, если верхняяя граница <= нижней
    elif gap > 1:
        count += 1
        predict = limit_min + int((limit_max - limit_min)/2)
        if number == predict:
            return count  # выход из цикла и возврат, если угадали
        elif number > predict:
            count = game_core_v2(number, count, predict, limit_max)
            return count
        else:
            count = game_core_v2(number, count, limit_min, predict)
            return count
    else:
        print('Error in limits')
        return 2000


def score_game(game_core):
    #  Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число
    count_ls = []
    random.seed(1)
    #  фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = [random.randint(1, 100) for i in range(11)]
    for number in random_array:
        count = 0
        #   print(f"Загадано число {number}")
        count_ls.append(game_core(number, count, 1, 100))
        #   print(count_ls)
    score = int(mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v2)
