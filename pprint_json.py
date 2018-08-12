import json
import sys


def load_data(filepath):
        with open(filepath, "r", encoding="utf-8") as json_file:
            return json.loads(json_file.read())


def pretty_print_json(json_object):
    print(
        json.dumps(
            json_object,
            sort_keys=True,
            indent=4,
            ensure_ascii=False,
            )
        )


def main():
    try:
        path_to_file = sys.argv[1]
        json_object = load_data(path_to_file)
        pretty_print_json(json_object)
    except IndexError:
        print("No path were provided")
    except OSError:
        print("File error")
    except ValueError:
        print("JSON file is not valid")


if __name__ == "__main__":
    main()
