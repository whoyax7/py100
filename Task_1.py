import json

INPUT_FILE = "input.json"

def task() -> float:
    with open(INPUT_FILE, "r") as f:
        json_data = json.load(f)

    return sum([item1["score"] * item1["weight"] for item1 in json_data])

print(f"{task():.3f}")
