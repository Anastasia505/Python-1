# Функция для нахождения общих участников
def find_common_participants(group1, group2, delimiter=","):
    set_group1 = set(group1.split(delimiter))
    set_group2 = set(group2.split(delimiter))

    common_participants = sorted(set_group1 & set_group2)
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверка функции с разделителем "|"
common = find_common_participants(participants_first_group, participants_second_group, delimiter="|")

# Вывод результата
print("Общие участники:", common)
