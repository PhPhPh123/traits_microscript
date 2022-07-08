from random import sample

list_traits = [
    'Проклятый снайпер. Критудачи и критнеудачи 3-6 и 15-18 в любом случае',
    'Толстокожий +25% ВУ',
    'Точный +1 точность',
    'Косой -1 точность',
    'Стреляет только очередями',
    'Всегда стреляет по самому слабому',
    '+3 скорость',
    'уменьшенный 2 раза урон от псионики',
    'есть механика псионики на выбор',
    'тупой - делает всякую хуйню',
    'перезаряжается после каждого выстрела',
    'механика удачи 2 раза в бой',
    '+25% ХП',
    '+2 уворот',
    '+1 уворот в ход',

]


def script(traits):
    user_input = input()
    user_list = list(user_input.split())
    if user_list[0] == 'roll':
        try:
            with open('traits.txt', 'w', encoding='utf-8') as t:
                num = int(user_list[1])
                choisen_traits = sample(traits, k=int(num+2))
                for elem in choisen_traits:
                    t.write(f'{elem}\n')
        except:
            print('Число должно быть целым')


if __name__ == '__main__':
    script(list_traits)
