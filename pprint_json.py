import json
import sys


def load_data(filepath):
        with open(filepath, "r", encoding="utf-8") as json_file:
            return json.loads(json_file.read())


def pretty_print_json(decoded_json):
    print(
        json.dumps(
            decoded_json,
            sort_keys=True,
            indent=4,
            ensure_ascii=False,
            )
        )


def main():
    try:
        path_to_file = sys.argv[1]
        decoded_json = load_data(path_to_file)
        pretty_print_json(decoded_json)
    except IndexError:
        print("No path were provided")
    except OSError:
        print("File error")
    except ValueError:
        print("JSON file is not valid")


if __name__ == "__main__":
    main()
