# launching via
# echo '<string>' | python lab2.py

import sys
import hashlib

def print_usage():
    print("Использование: echo 'password' | python blf_crypt_hash.py")

def main():
    if sys.stdin.isatty():
        print("Ошибка: Нет данных из стандартного ввода.")
        print_usage()
        sys.exit(1)

    input_data = sys.stdin.read().strip()

    if not input_data:
        print("Ошибка: Введены пустые данные.")
        sys.exit(1)

    try:
        hashed = hashlib.sha256(input_data.encode('utf-8')).hexdigest()
        print(hashed)
    except Exception as e:
        print(f"Ошибка при генерации хеша: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()