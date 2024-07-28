import sys
import os
import subprocess


def print_usage():
    print("Usage: python3 script.py <url_file> <headers_file>")


def main(url_file, headers_file):
    # Проверка существования файлов
    if not os.path.isfile(url_file):
        print(f"Error: URL file '{url_file}' does not exist.")
        sys.exit(1)

    if not os.path.isfile(headers_file):
        print(f"Error: Headers file '{headers_file}' does not exist.")
        sys.exit(1)

    # Чтение файла строка за строкой
    with open(url_file, "r") as f:
        urls = f.readlines()

    # Выполнение команды для каждого URL
    for url in urls:
        url = url.strip()  # Удаление лишних пробелов и символов новой строки
        if url:
            subprocess.run(["headerpwn", "-url", url, "-headers", headers_file])


if __name__ == "__main__":
    # Проверка наличия аргументов
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(1)

    # Параметры
    url_file = sys.argv[1]
    headers_file = sys.argv[2]

    main(url_file, headers_file)
