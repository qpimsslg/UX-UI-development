# запуск через терминал и команду
# python lab1.py <first_file.txt> <second_file.txt> <output_file.txt>

import os
def merge_files(file1_path, file2_path, output_path):
    try:
        if not os.path.exists(file1_path):
            print(f"Ошибка: файл '{file1_path}' не найден.")
            return

        if not os.path.exists(file2_path):
            print(f"Ошибка: файл '{file2_path}' не найден.")
            return

        if os.path.exists(output_path):
            response = input(f"Файл '{output_path}' уже существует. Перезаписать? (y/n): ").strip().lower()
            if response != 'y':
                print("Операция отменена.")
                return

        try:
            with open(file1_path, 'r', encoding='utf-8') as file1, \
                 open(file2_path, 'r', encoding='utf-8') as file2, \
                 open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(file1.read())
                output_file.write("\n")  # Добавляем перевод строки между файлами
                output_file.write(file2.read())

            print(f"Файлы успешно объединены в '{output_path}'.")

        except PermissionError:
            print(f"Ошибка: недостаточно прав для записи в файл '{output_path}'.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Объединение двух текстовых файлов в третий.")
    parser.add_argument("file1", help="Путь к первому входному файлу.")
    parser.add_argument("file2", help="Путь ко второму входному файлу.")
    parser.add_argument("output", help="Путь к выходному файлу.")

    args = parser.parse_args()

    merge_files(args.file1, args.file2, args.output)