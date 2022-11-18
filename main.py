# freelanceTask7

# Описание
#
# Питон, теория вероятности, метод Монте Карло
# Решение задач.
# Решить задачи с комментариями

# 1. Игральная кость независимо бросается два раза. X - сумма выпавших значений.
# Найти распределение X (множество возможных значений и соответствующие вероятности).
# Проверить ответ, оценив вероятность с помощью метода Монте-Карло

# **********************************************************************************************************************
# Возможные значения одной кости: от 1 до 6, двух - от 2 до 12. Число комбинаций одной кости - 6,двух - 36
# Вероятность выпадения 2 = '1' + '1' - 1/36, 12 = '6'+ '6' - 1/36, 3 = '1' + '2' или '2' + '1' / 36 и т.д

bone_values_list = [1, 2, 3, 4, 5, 6]  # возможные значения кости
dropped_values_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # возможные суммы выпавших значений двух костей

# число комбинаций двух костей, дающих заданное возможное значение суммы
combination_count_list = []  # список с числом комбинаций
for i in range(len(dropped_values_list)):
    combination_count = 0  # число комбинаций, например: '2'='1'+'1' => 1
    for j in range(len(bone_values_list)):
        for n in range(len(bone_values_list)):
            if dropped_values_list[i] == bone_values_list[j] + bone_values_list[n]:
                combination_count += 1
    combination_count_list.append(combination_count)

# Распределение X (множество возможных значений и соответствующие вероятности).
x_out = {}  # словарь "распределение X"
for i, value in enumerate(dropped_values_list):
    x_out[value] = float(combination_count_list[i] / 36)

print(x_out)

# Проверяем ответ, оценив вероятность с помощью метода Монте-Карло
import numpy
from numpy import random


def dice():
    # функция выдает случайное число от 1 до 6 включительно
    return random.randint(1, 7)


def diceroll(number_of_times):
    # Вводишь количество бросков двух кубиков, и получаешь распределение: "число очков:число выпавших случаев"
    counter = {n: 0 for n in range(2, 13)}  # Словарь-счетчик. Все ключи изначально = 0
    for i in range(number_of_times):
        first_dice = dice()
        second_dice = dice()
        total = first_dice + second_dice
        counter[total] += 1  # при выпадении определенного количества очков, счетчик с таким ключом увеличивается
    return counter

print(diceroll(100))
