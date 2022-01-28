
def analyse(programm: list[tuple[str, int]]) -> int:
    # Создание списка на отгрузку
    unload = []
    for action in programm:
        if action[0] == 'выгрузить':
            unload.append(action[1])

    # Процесc расфосовки ящиков
    result = 0
    unload_row = []
    for action in programm:
        if action[0] == 'принять':
            if action[1] in unload:
                unload_row.append(action[1])
            result += 1
        else:
            if len(unload_row) == 1:
                result += 1
                unload_row.clear()
            else:
                # Получение количество элементов необходимых достать
                index_box = unload_row.index(action[1])
                coun_unload = len(unload_row) - (index_box + 1)
                result += 2 * coun_unload + 1
                del unload_row[index_box]
    return result


def main():
    result = analyse([
        ('принять', 1),
        ('принять', 2),
        ('выгрузить', 1),
        ('принять', 3),
        ('принять', 4),
        ('выгрузить', 3),
    ])
    return result


if __name__ == "__main__":
    print(main())
