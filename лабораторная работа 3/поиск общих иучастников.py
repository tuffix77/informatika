# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


def find_common_participants(group1, group2, separator=','): # определяем функцию по 3 параметрам

    list1 = [name.strip() for name in group1.split(separator)] # получаем список фамилий 1 группы


    list2 = [name.strip() for name in group2.split(separator)] # то же самое со 2 группой

    # преобразуем в множэество

    set1 = set(list1)
    set2 = set(list2)


    common_set = set1 & set2     # ищем совпадения


    common_list = list(common_set)   # преобразуем обратно в список


    common_list.sort()   # сортируем по алфавиту


    return common_list   # возвращаем отсортированный список



participants_first_group = "Иванов | Петров | Сидоров"   # 1 группа участников

participants_second_group = "Петров | Сидоров | Смирнов"   # 2я


common_participants = find_common_participants(
    participants_first_group,
    participants_second_group,
    separator=" | "    # проверяем функцию с другим разделителем
)


print("Общие участники:", common_participants)   # принт так сказать печатаем

# TODO Провеьте работу функции с разделителем отличным от запятой
