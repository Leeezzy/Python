print('Привет! Хочу показать тебе, что я уже умею делать!')
new_list = input('Введи любые целые числа. Разделяй их пробелом! :) ').split()
print('Давай я повторю:', new_list)
print('А теперь смотри! Я поменяю соседние элементы местами!')
print('Вжух!')
for i in range(1, len(new_list), 2):
    new_list[i - 1], new_list[i] = new_list[i], new_list[i - 1]
print(new_list)





