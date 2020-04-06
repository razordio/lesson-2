items = []
attribs = {'название': '', 'цена': '', 'количество': '', 'ед': ''}
analitics = {'название': [], 'цена': [], 'количество': [], 'ед': []}
num = 1
while True:
    for a in attribs.keys():
        item = input('Веедите {} товара: '.format(a))
        attribs[a] = item
        analitics[a].append(attribs[a])
    items.append((num, attribs))
    num += 1
    if input('Продолжить ввод данных (ДА) или вывести аналитику (НЕТ)').upper() == 'НЕТ':
        print('Список товаров\n', items)
        print('Текущая аналитика\n',analitics)
        break

