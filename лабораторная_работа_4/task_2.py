import json

INPUT_FILENAME = "input.json"

def task() -> float:
    # Чтение JSON файла
    with open(INPUT_FILENAME, mode="r", encoding="utf-8") as json_file:
        data = json.load(json_file)  # Загрузка данных в виде списка словарей

    # Вычисление суммы произведений
    total_sum = sum(item["score"] * item["weight"] for item in data)

    # Возвращаем сумму, округлённую до 3 знаков
    return round(total_sum, 3)


print(task())
