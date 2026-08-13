import json
from pathlib import Path


def read_json(file_path):
    encoding = 'utf-8'
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data
def write_json(data, file):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

data = read_json(Path("./data/pytopia.json"))
data['messages'] = data['messages'][:1000]  # Limit the message to the first 100 characters
write_json(data, Path("./data/pytopia_short.json"))