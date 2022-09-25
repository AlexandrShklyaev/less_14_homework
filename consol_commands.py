def get_filter(list_lines: list, condition: str) -> list:
    return list(filter(lambda x: x.find(condition) >= 0, list_lines))


def get_sort(list_lines: list, is_reverse: bool = False) -> list:
    return sorted(list_lines, reverse=is_reverse)


def get_map(list_lines: list, column: int) -> list:
    return list(map(lambda x: "".join(x.split()[column:column + 1]), list_lines))
    # т.к. в строках разное количество столбцов, то используем срез [column:column + 1], а не индекс


def get_unique(list_lines: list) -> list:
    return list(set(list_lines))


def get_limit(list_lines: list, limit: int) -> list:
    return list_lines[:max(limit, 0)]


def get_maps(list_lines: list, columns: str) -> list:  # дополнительная команда
    """ выводит несколько столбцов через пробел (например, maps 0 4 7) """
    list_col = columns.split()
    return list(map(lambda x: " ".join(map(lambda y: "".join(x.split()[int(y):(int(y) + 1)]), list_col)), list_lines))


def run_comand(list_lines: list, command: str, atribute: str) -> list:
    """ для текущего списка строк выполняет команду по её имени и параметру """
    if atribute == "":
        print(f"вы не указали параметр для команды '{command}'")
        print("примеры: filter abc | unique - | sort asc | sort desc| limit 5 | map 3 | maps 0 6 3 22 8")
        return []
    if command == "filter":
        return get_filter(list_lines, atribute)
    if command == "map":
        return get_map(list_lines, int(atribute))
    if command == "unique":
        return get_unique(list_lines)
    if command == "sort":
        if atribute == "asc":
            return get_sort(list_lines)
        if atribute == "desc":
            return get_sort(list_lines, True)
    if command == "limit":
        return get_limit(list_lines, int(atribute))
    if command == "maps":
        return get_maps(list_lines, atribute)
    print("неизвестная команда")
    return []
