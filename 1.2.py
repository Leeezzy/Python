time = int(input("Введите число в секундах: "))
hours = time // 3600
seconds = time - hours * 3600
minutes = seconds // 60
secs = seconds - minutes * 60
print(f"{hours} : {minutes} : {secs}")