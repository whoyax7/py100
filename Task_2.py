import json
import csv
from io import StringIO


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as csv_f:
        csv_data = csv.DictReader(csv_f,)
        csv_data_list = list(csv_data)
        with open(OUTPUT_FILENAME, "w", encoding='utf-8') as json_f:
            return json.dump(csv_data_list, json_f, indent = 4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
