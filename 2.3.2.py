my_month = int(input('Введите, пожалуйста, порядковый номер месяца, а я подскажу, к какому времени года он относится:)            '))
my_list = ['Это зима', 'Это весна', 'Это лето', 'Это осень']
if my_month >= 3 and my_month <= 5:
    print(my_list(1))
elif my_month >= 6 and my_month <=8:
    print(my_list(2))
elif my_month >= 7 and my_month <= 11:
    print(my_list(3))
else:
    print(my_list(0))

