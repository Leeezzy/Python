new_list = [9, 8, 6, 6, 2, 2, 2]
v = print(int(input(f'Привет, введи любое натуральное число  ')))
v = ''.isdigit
i = 0
    for v in new_list:
        if v > n:
            i += 1
        elif v < new_list[i]:
            new_list.insert(i - 1, v)
        else:
            new_list.append(v)
            break
print(new_list)