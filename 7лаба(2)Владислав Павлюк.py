#Задача. Вивести дані про книги, тираж яких не перевищує 10000 примірників. Поля
#структури: Автор, Жанр, Назва, Тираж.
#Павлюк Владислав 122-в
while True:
    while True:
        try:
          y=int(input('Введите тираж 1 книги'))  
          x=int(input('Введите тираж 2 книги'))  
          break
        except ValueError:
            print('Введите число')
    keys=['author','title','genre','edition']
    a=[input('Введите автора 1 книги '),input('Введите название 1 книги '),input('Введите жанр 1 книги '),y]
    b=[input('Введите автора 2 книги '),input('Введите название 2 книги '),input('Введите жанр 2 книги '),x]
    slov={keys:a for(keys,a) in zip(keys,a) if y>10000}
    slov2={keys:b for(keys,b) in zip(keys,b) if x>10000}
    print(slov,slov2)
    result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
    if result == '1':
        continue
    else:
        break
