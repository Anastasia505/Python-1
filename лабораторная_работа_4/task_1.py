import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Чтение содержимого CSV файла
    with open(INPUT_FILENAME, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=",")
        data = [row for row in csv_reader]

    # JSON файл с отступами
    with open(OUTPUT_FILENAME, mode="w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
