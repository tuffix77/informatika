# TODO Напишите функцию для поиска индекса товара


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
def find_item_index(items_list, find_item): # определяем функцию по списку товаров и искомому товару

    for i, item in enumerate(items_list): # i получает индекс элемента, item получает значение элемента

        if item == find_item: # совпадает ли даннфй элемент с искомым

            return i

    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан'] # список товаров

for find_item in ['банан', 'груша', 'персик']: #цикл по списку товаров

    index_item = find_item_index(items_list, find_item)  # резкльтат сохраняем в переменную index_item

    if index_item is not None:

        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")  # еслди товар найден
    else:

        print(f"Товар '{find_item}' не найден в списке.")  # если не найден