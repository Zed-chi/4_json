import json
import sys


def load_data(filepath):
    try:
        with open(filepath, "r", encoding='utf-8') as f:
            return json.loads(f.read())
    except OSError:
        print("invalid path")


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4))


if __name__ == '__main__':
    path_to_file = sys.argv[1]
    json_data = load_data(path_to_file)
    pretty_print_json(json_data)
