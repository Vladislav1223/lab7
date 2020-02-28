#Дана послідовність n, що складається з символів s1, s2, .... Обрахувати загальну
#кількість входжень символів +, -, * у послідовність.
#Павлюк Владислав 122-в
while True:
  a=input('Введите символы ')
  b={'+','-','*'}
  b_set=set(b)
  count=0
  for i in range(len(a)):
      if a[i] in b_set:
        count+=1
  print(count)
  result = input('Хотите продолжить? Если да - 1, Если нет - інше: ')
  if result == '1':
        continue
  else:
        break
