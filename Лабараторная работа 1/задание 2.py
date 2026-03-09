list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
# находим колво игроков
t_play = len(list_players)

# индекс середины
middle_index = t_play // 2

# разбиваем на команды

first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

# выводим команды

print(first_team)
print(second_team)
