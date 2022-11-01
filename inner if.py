age = int(input('Input your age: '))

if age < 18:
    print('Ждем тебя в школе')
elif age >= 18 and age <=30:
    print('Иди в универ')
elif age > 30 and age < 40:
    print('Иди на работу')
    job = input('Your job: ')
    if job == 'Progger':
        print('Иди прогать!')

else:
    print('Больше 40 лет')
print('end')