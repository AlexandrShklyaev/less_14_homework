from consol_commands import *


def get_lines_of_file(filename: str) -> list:
    """ возвращает содержимое файла в виде списка строк """
    if filename == "":
        filename = "data/apache_logs.txt"
    print(f"выбран файл '{filename}'")
    with open(filename, "r", encoding="utf-8") as file:
        return [x.strip() for x in file.readlines()]


def get_comands(list_lines: list, list_comands: list[str]) -> list:
    """ вызывает команды по очереди из списка команд """
    for each in list_comands:
        text_comand = each.strip().split()
        comand = text_comand[0]
        atribute = " ".join(text_comand[1:])
        list_lines = run_comand(list_lines, comand, atribute)
    return list_lines


def main() -> None:
    print("Добро пожаловать. Введите путь к локальному файлу или оставьте пустым")
    filename = input(">>> ")  # если оставить пустым, то будет выбран файл 'data/apache_logs.txt'
    list_lines = get_lines_of_file(filename)
    while True:
        print("-" * 60)
        print("список возможных команд:  filter | unique | sort | limit | map | maps")
        print("введите стоп или команды, разделяя их |")
        list_comands = input(">>> ").split("|")
        if list_comands == "стоп":
            break
        rezult = get_comands(list_lines, list_comands)
        for each_line in rezult:
            print(each_line)


if __name__ == '__main__':
    main()
