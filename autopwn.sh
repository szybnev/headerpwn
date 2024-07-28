#!/bin/bash

# Проверка наличия аргументов
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <url_file> <headers_file>"
  exit 1
fi

# Параметры
url_file="$1"
headers_file="$2"

# Проверка существования файлов
if [ ! -f "$url_file" ]; then
  echo "Error: URL file '$file' does not exist."
  exit 1
fi

if [ ! -f "$headers_file" ]; then
  echo "Error: Headers file '$headers_file' does not exist."
  exit 1
fi

# Чтение файла строка за строкой
while IFS= read -r url; do
  # Выполнение команды для каждого URL
  headerpwn -url "$url" -headers "$headers_file"
done < "$url_file"
