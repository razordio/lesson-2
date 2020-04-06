start_list = list(input('Заполните список: '))
print(start_list)

for i in range(1, len(start_list), 2):
    start_list[i - 1], start_list[i] = start_list[i], start_list[i - 1]
print(start_list)