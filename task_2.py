def find_common_participants(participants_first_group, participants_second_group, separator = ','):
    first_group = set(participants_first_group.split('|'))
    second_group = set(participants_second_group.split('|'))
    join_group = list(first_group.intersection(second_group))
    join_group.sort()
    join_group.insert(1, separator)
    return join_group


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group,participants_second_group, '*'))
