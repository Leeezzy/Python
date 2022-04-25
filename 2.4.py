my_str = input(str('Введи несколько слов, разделяя их пробелами:   ')).split()
for i, word in enumerate(my_str, 1):
    print(f'{i}). {word[:10]}')





