# TODO Найдите количество книг, которое можно разместить на дискете
sym = 4
line = 25 * sym
#print('Количество символов в строке (байт):', line)
count_line = line * 50
#print('Количество символов на странице (байт):', count_line)
page = count_line * 100
#print('Количество символов в книге (байт):', page)
volume = 1.44 * 1024 * 1024
#print('Объем дискеты в байтах:', volume)

books = round(volume / page)



print("Количество книг, помещающихся на дискету:", books)
