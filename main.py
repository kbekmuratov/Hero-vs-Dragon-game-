import random

dragon = {
    'hp': 2000,
    'defence': 150,
    'str': 150,
    'weapon': 0
}

hero = {
    'hp': 1000,
    'defence': 100,
    'str': 150,
    'weapon': 250,
    'shield': 150,
    'has_shield': False,
    'potions': 1
}


def display_dragon_info():
    print(f"Здоровье дракона: {dragon['hp']} HP")


def display_hero_info():
    print(f"Здоровье героя: {hero['hp']} HP, "
          f"Защита: {hero['defence']}, Зелий: {hero['potions']}")


def modify_health(character, amount):
    character['hp'] += amount
    if character['hp'] < 0:
        character['hp'] = 0


def hero_attack():
    hero_hit_chance = random.randint(1, 100)
    if hero_hit_chance <= 75:
        damage = hero['str'] + hero['weapon'] - dragon['defence']
        modify_health(dragon, -damage)
        print(f"Герой попал! Дракон получил {damage} ед. урона.")
    else:
        print("Герой промахнулся.")


def use_potion():
    if hero['potions'] > 0:
        modify_health(hero, 500)
        hero['potions'] -= 1
        print("Герой выпил зелье и восстановил 500 единиц здоровья.")
    else:
        print("У героя нет зелий.")


def dragon_attack():
    dragon_hit_chance = random.randint(1, 2)
    if dragon_hit_chance == 1:
        damage = dragon['str'] + dragon['weapon'] - hero['defence']
        modify_health(hero, -damage)
        print(f"Дракон атакует! Герой получил {damage} ед. урона.")
    else:
        print("Дракон проспал свой ход.")


def dragon_fireball():
    if random.randint(1, 2) == 1:
        damage = dragon['str'] * 2
        if hero['has_shield']:
            damage = 0
            print("Герой отразил огненный шар щитом!")
        modify_health(hero, -damage)
        if damage > 0:
            print(f"Дракон плюется огненным шаром! Герой получил "
                  f"{damage} ед. урона.")
    else:
        dragon_attack()

    if dragon['hp'] > 1500:
        print(f"Здоровье дракона:{dragon['hp']} HP / Дракон чувствует себя как на празднике,"
              " готов дышать огнём!")
    elif dragon['hp'] > 500:
        print(f"Здоровье дракона: {dragon['hp']} HP / Дракон устал, но ещё не готов сдаться. "
              "Нужно немного подзарядиться!")
    elif dragon['hp'] > 300:
        print(f"Здоровье дракона: {dragon['hp']} HP / Дракон кажется напряжённым, но ещё "
              "может показать класс на арене!")
    else:
        print(f"Здоровье дракона: {dragon['hp']} HP (Осторожно! Дракон еле дышит, "
              "как будто съел огненный перчик!")

    display_hero_info()


print("Добро пожаловать в игру 'Битва Героя и Дракона!'")
print("Приготовьтесь к эпической схватке!\n")


while True:
    print("=" * 50)
    print("Ход героя:" + '\n')
    print("Выберите действие для героя:")
    print("1 - Атаковать (attack)")
    print("2 - Защититься (defend)")
    print("3 - Пропустить ход (pass)")
    print("4 - Использовать зелье (use potion)")

    hero_action = input("Введите номер действия: ").strip()

    if hero_action == "1":
        hero_attack()
    elif hero_action == "2":
        hero['has_shield'] = True
        print("Герой защищается!")
    elif hero_action == "3":
        print("Герой пропустил ход.")
    elif hero_action == "4":
        use_potion()
    else:
        print("Некорректное действие. Пожалуйста, введите номер от 1 до 4.")

    display_dragon_info()
    display_hero_info()
    print('\n')

    if dragon['hp'] <= 0:
        print("Герой поднял меч вверх, победив зловещего дракона! ")
        break

    dragon_fireball()
    if hero['hp'] <= 0:
        print("Герой был повержен, но его история еще не закончена!")
        break

    if hero['has_shield']:
        hero['has_shield'] = False
        print("Герой убрал щит.")
